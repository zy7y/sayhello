from fastapi import FastAPI
from sqlalchemy import func
from starlette.middleware.cors import CORSMiddleware

from schemas import *
from db import session
import models

app = FastAPI(title="SayHello(留言板)",
              description="""
              翻自 《Flask Web开发实战_入门、进阶与原理解析（李辉著 ）》 中的实战项目SayHello
              原版Github: https://github.com/greyli/sayhello
              """
              )

# 设置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/index", name="欢迎首页")
async def index():
    return {"msg": "欢迎来到SayHello!"}


@app.post("/message", name="添加留言", response_model=Response200)
async def add_message(message: MessageCreate):
    message_obj = models.Message(
        name=message.name,
        body=message.body
    )
    session.add(message_obj)
    session.commit()
    session.refresh(message_obj)
    return Response200(data=message_obj)


@app.get("/message", name="分页获取留言列表", response_model=ResponseList200)
async def get_messages(limit: int = 5, page: int = 1):
    # 统计条数
    total = session.query(func.count(models.Message.id)).scalar()
    skip = (page - 1) * limit   # 计算当前页的起始数
    # 倒序显示
    data = session.query(models.Message).order_by(models.Message.create_at.desc()).offset(skip).limit(limit).all()
    return ResponseList200(total=total, data=data)
