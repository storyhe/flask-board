from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from members.database import Base

class User(Base):
    __tablename__ = 'Users'
    idx = Column(Integer, primary_key=True)
    userid = Column(String(50), unique=True)
    password = Column(String(250))
    nickname = Column(String(250))
    regdate = Column(DateTime, nullable=False, default=datetime.utcnow)

class Board(Base):
    __tablename__ = 'Board'
    id = Column(Integer, primary_key=True)
    boardId = Column(String(250))
    member_idx = Column(Integer)
    name = Column(String(250))
    title = Column(String(250))
    content_body = Column(Text)
    regdate = Column(DateTime, nullable=False, default=datetime.utcnow)

