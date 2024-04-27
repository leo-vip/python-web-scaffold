from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from core.db_core import engine

Base = declarative_base()


class TUser(Base):
    __tablename__ = "t_user"

    id = Column(String(128), primary_key=True)
    name = Column(String(64), )
    email = Column(String(64), unique=True)
    password = Column(String(256), )
    create_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    status = Column(Integer, default=0)
    memo = Column(String(1024), comment="描述")

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


# initial
Base.metadata.create_all(engine)
