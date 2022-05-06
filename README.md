# SayHello - Bottle
该版本使用 [Bottle](http://bottlepy.org/docs/dev/) 构建接口服务
>Bottle is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.
[Web Frameworks Benchmark](https://web-frameworks-benchmark.netlify.app/result?l=python)
____
>Bottle 是一个快速、简单、轻量级的 Python WSGI 微型 Web 框架。它只有一个文件，只依赖 Python 标准库 。

**仅Docker部署时才会安装第三方包`gunicorn` `meinheld`, [部署选型参考](https://github.com/the-benchmarker/web-frameworks/blob/master/python/bottle/config.yaml)**

# 本地运行
```shell
git clone -b bottle-sayhello https://github.com/zy7y/sayhello.git
python main.py 
浏览器访问: http://localhost:8000/message
```

# docker部署
**确保已经安装docker**
```shell
git clone -b bottle-sayhello https://github.com/zy7y/sayhello.git
cd sayhello
sh deploy.sh
浏览器访问: http://部署服务器IP:8000/message
```

# api
```shell
GET /message?limit=5&page=1
查询参数 limit - 每页显示条数, page - 当前页码

POST /message
json参数 {
    "name": 1,
    "body": 1
}
```