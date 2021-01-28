from datetime import datetime

from fastapi import Body
from pydantic import BaseModel

from typing import List


class MessageBase(BaseModel):
    name: str = Body(..., min_length=2, max_length=8)
    body: str = Body(..., min_length=1, max_length=200)


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int = None
    create_at: datetime

    class Config:
        orm_mode = True


class Response200(BaseModel):
    code: int = 200
    msg: str = "操作成功"
    data: Message = None


class ResponseList200(Response200):
    total: int
    data: List[Message]


class Response400(Response200):
    code: int = 400
    msg: str = "无数据返回"
