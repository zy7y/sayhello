# 测试API
import operator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from main import app, session

client = TestClient(app)


def test_index():
    response = client.get("/index")
    assert response.status_code == 200
    assert response.json() == {"msg": "欢迎来到SayHello!"}


@pytest.mark.parametrize("skip, limit", [[1, 2], [1, 10], [-1, 5]])
def test_get_message(skip, limit):
    response = client.get("/message", params={"skip": skip, "limit": limit})
    assert response.status_code == 200
    sql = "select * from message order by create_at desc limit :skip,:limit"
    data = session.execute(text(sql), {"skip": skip, "limit": limit}).fetchall()
    assert response.json()['data'][0]["id"] == data[0]["id"]


@pytest.mark.parametrize("data", [{"name": "七七", "body": "回踩!"}])
def test_add_message(data):
    response = client.post("/message", json=data)
    assert response.status_code == 200
    sql = "select * from message where name = :name"
    result = session.execute(text(sql), {"name": data["name"]}).fetchall()
    assert result is not None
