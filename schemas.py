from pydantic import BaseModel, validator, constr
from datetime import datetime
from typing import Type, Any


class BaseException(Exception):
    pass


class User(BaseModel):
    fam: str
    name: str
    otc: str = None
    phone: str = None
    email: str

    @validator('email')
    def validate_email(cls: Type['User'], value: str) -> str:
        if not all(char in value for char in ['@', '.']):
            raise BaseException('The email is wrong')
        return value

    @validator('phone')
    def validate_phone(cls: Type['User'], value: str) -> str:
        if not all(digit.isdigit() for digit in value):
            raise BaseException('The phone number is wrong')
        return value


class Coordinate(BaseModel):
    latitude: float
    longitude: float
    height: int


class Level(BaseModel):
    winter: constr(max_length=2) = None
    summer: constr(max_length=2) = None
    autumn: constr(max_length=2) = None
    spring: constr(max_length=2) = None


class Image(BaseModel):
    title_1: str = None
    image_1: str
    title_2: str = None
    image_2: str
    title_3: str = None
    image_3: str = None


class Pass(BaseModel):
    add_time: datetime
    beauty_title: str
    title: str
    other_titles: str = None
    connect: str = None
    status: str = "New"

    class Config:
        orm_mode = True