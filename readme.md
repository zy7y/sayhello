# 简介
> 翻自 《Flask Web开发实战_入门、进阶与原理解析（李辉著 ）》 中的实战项目SayHello
**线上体验地址:http://49.232.203.244:9001/message.html**

# 图片加载不出来
所有图片都是用的gitee做图床，不知道为什么github展示不出来，需要看图片请前往
[该项目的Gitee仓库地址](https://gitee.com/zy7y/sayhello)
# 技术栈
FastAPI + SQLAlchemy(sqlite3) + html + css + vue.js + axios
# 动态
1. 新增留言， 留言列表接口, 接口测试
2. 完善前端页面,更改实时校验，https://blog.csdn.net/qq_22182989/article/details/103728781
3. 体验版部署，更新docker 部署文档
# 本地启动
1. 项目目录下执行`pip install -r requirements.txt`
2. `Terminal(终端)`执行命令`uvicorn main:app --reload`
3. 访问服务
- http://127.0.0.1:8000/docs    # 接口文档

# docker部署
**详细内容请看：https://www.cnblogs.com/zy7y/p/14344375.html**

## 后端部署
1. 进入到项目目录下(命令请在命令行执行)
2. 执行`docker build -t sayhello .`
3. 运行容器`docker run -d --name sayhello-fastapi -p 8000:80 sayhello`

## 前端部署
**需要确定static/message.html 中的 `baseURL`地址是不是后端服务器IP地址**
![](https://gitee.com/zy7y/blog_images/raw/master/img/20210129124621.png)
1. 进入到项目static目录下
2. 执行`docker build -t sayhello-front .`
3. 运行容器`docker run -d --name sayhello-front-9000 -p 9001:80 sayhello-front`

## 访问 IP:9001/message.html
![](https://gitee.com/zy7y/blog_images/raw/master/img/20210129124425.png)
