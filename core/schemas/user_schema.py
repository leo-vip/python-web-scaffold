import datetime
from typing import Union, Any

from pydantic import  validator
from pydantic.main import BaseModel


# https://fastapi.tiangolo.com/zh/tutorial/response-model/


class UserOut(BaseModel):
    id: Union[Any, None] = None
    name: Union[Any, None] = None
    email: Union[Any, None] = None
    create_time: datetime.datetime = None

    class Config:
        orm_mode = True

    @validator('create_time')
    def set_create_now(cls, v: datetime.datetime):
        return str(int(v.timestamp() * 1000))


class UserIn(BaseModel):
    name: Any = None
    email: Any
    password: Any

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: Union[Any, None] = None


class APITokenData(BaseModel):
    source_id: Union[Any, None] = None
