# 使用说明
1. 安装依赖包
```shell
python -m venv venv
**win**
venv\Scripts\activate
pip install -r requirements.txt
   
```

2. 执行迁移命令
```shell
python manage.py makemigrations sayHello
python manage.py migrate
```
3. 创建后台账号
   
```shell
python manage.py createsuperuser

```
3. 启动服务
```shell
python manage.py runserver
```
3.1 index.html为前端

4. 访问管理系统
http://127.0.0.1:8000/admin
   
5. 访问可用接口列表
http://127.0.0.1:8000/
   
6. swaager接口列表
http://127.0.0.1:8000/swagger