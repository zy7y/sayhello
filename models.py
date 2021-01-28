from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer

# 得到默认Base基类
Base = declarative_base()


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), comment="昵称", nullable=False)
    body = Column(String(200), comment="内容", nullable=False)
    create_at = Column(DateTime, default=datetime.now, comment="创建时间")
