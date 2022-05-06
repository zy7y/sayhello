import json
import logging

from bottle import Bottle, HTTPError, PluginError, request, response

logging.disable()
try:
    from meinheld import patch

    patch.patch_all()
except ImportError:
    pass

import inspect
import sqlite3


class SQLitePlugin(object):
    """This plugin passes an sqlite3 database handle to route callbacks
    that accept a `db` keyword argument. If a callback does not expect
    such a parameter, no connection is made. You can override the database
    settings on a per-route basis."""

    name = "sqlite"
    api = 2

    def __init__(self, dbfile=":memory:", autocommit=True, dictrows=True, keyword="db"):
        self.dbfile = dbfile
        self.autocommit = autocommit
        self.dictrows = dictrows
        self.keyword = keyword

    def setup(self, app):
        """Make sure that other installed plugins don't affect the same
        keyword argument."""
        for other in app.plugins:
            if not isinstance(other, SQLitePlugin):
                continue
            if other.keyword == self.keyword:
                raise PluginError(
                    "Found another sqlite plugin with "
                    "conflicting settings (non-unique keyword)."
                )

    def apply(self, callback, context):
        # Override global configuration with route-specific values.
        conf = context.config.get("sqlite") or {}
        dbfile = conf.get("dbfile", self.dbfile)
        autocommit = conf.get("autocommit", self.autocommit)
        dictrows = conf.get("dictrows", self.dictrows)
        keyword = conf.get("keyword", self.keyword)

        # Test if the original callback accepts a 'db' keyword.
        # Ignore it if it does not need a database handle.
        # args = inspect.getargspec(context.callback)[0]
        args = inspect.getfullargspec(context.callback)[0]
        if keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            # Connect to the database
            db = sqlite3.connect(dbfile)
            # This enables column access by name: row['column_name']
            if dictrows:
                db.row_factory = sqlite3.Row
            # Add the connection handle as a keyword argument.
            kwargs[keyword] = db

            try:
                rv = callback(*args, **kwargs)
                if autocommit:
                    db.commit()
            except sqlite3.IntegrityError as e:
                db.rollback()
                raise HTTPError(500, "Database Error", e)
            finally:
                db.close()
            return rv

        # Replace the route callback with the wrapped one.
        return wrapper


app = Bottle()

app.install(SQLitePlugin(dbfile="db.sqlite"))


@app.hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"


@app.get("/message")
def select(db):
    limit = int(request.params.get("limit", 5))
    page = int(request.params.get("page", 1))

    result = db.execute(
        "SELECT id, name, body, create_at FROM msg WHERE is_del = 0 ORDER BY create_at DESC LIMIT ?,?",
        (
            (page - 1) * limit,
            limit,
        ),
    )
    return {
        "code": 200,
        "msg": "操作成功",
        "data": [dict(row) for row in result],
        **dict(
            db.execute("SELECT COUNT(1) AS total FROM msg WHERE is_del = 0").fetchone()
        ),
    }


@app.post("/message")
def create(db):
    name = request.json["name"]
    body = request.json["body"]
    db.execute(
        "INSERT INTO msg ('name', 'body') VALUES (?, ?)",
        (
            name,
            body,
        ),
    )
    return {"code": 200, "msg": "操作成功", "data": None}


@app.delete("/message/<id:int>")
def remove(id: int, db):
    if request.get_header("is_admin") == "TrUe":
        db.execute(f"UPDATE msg set is_del=1 where id=?", (id,))
        db.commit()
        return {"code": 200, "msg": "操作成功", "data": None}
    else:
        return {"code": 403, "msg": "无权操作", "data": None}


# 重写异常
@app.error(code=404)
def error_404(e):
    response.content_type = "application/json"
    return json.dumps({"code": 404, "msg": "资源不存在", "data": None})


@app.error(code=405)
def error_405(e):
    response.content_type = "application/json"
    return json.dumps({"code": 405, "msg": "请求方法错误", "data": None})


@app.error(code=500)
def error_500(e):
    response.content_type = "application/json"
    return json.dumps({"code": 500, "msg": "内部错误", "data": None})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, reloader=True, debug=True)
    """
    gunicorn 服务器部署性能更高, 不支持windows
    gunicorn --log-level warning --bind 0.0.0.0:3000  --reuse-port --workers $(nproc) --worker-class meinheld.gmeinheld.MeinheldWorker main:app
    """
