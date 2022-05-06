FROM python:3.9.6
COPY . /app
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /app
RUN pip install --no-cache-dir gunicorn meinheld -i https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 80
# 为了在使用Gunicorn时提高性能，我们必须牢记3种并发方式。
# https://blog.csdn.net/pushiqiang/article/details/117197014
CMD ["gunicorn", "main:app","--log-level", "warning", "--bind", "0.0.0.0:80","--reuse-port","--workers","5", "--worker-class", "meinheld.gmeinheld.MeinheldWorker"]
