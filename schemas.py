from pydantic import BaseModel, validator, constr, EmailStr
from datetime import datetime
from typing import Type


class BaseException(Exception):
    pass


class UserScheme(BaseModel):
    fam: str
    name: str
    otc: str = None
    phone: str = None
    email: EmailStr

    @validator('email')
    def validate_email(cls: Type['UserScheme'], value: str) -> str:
        if not all(char in value for char in ['@', '.']):
            raise BaseException('The email is wrong')
        return value

    @validator('phone')
    def validate_phone(cls: Type['UserScheme'], value: str) -> str:
        if not all(digit.isdigit() for digit in value):
            raise BaseException('The phone number is wrong')
        return value


class CoordinateScheme(BaseModel):
    latitude: float
    longitude: float
    height: int


class LevelScheme(BaseModel):
    winter: constr(max_length=2) = None
    summer: constr(max_length=2) = None
    autumn: constr(max_length=2) = None
    spring: constr(max_length=2) = None


class ImageScheme(BaseModel):
    title_1: str = None
    image_1: str
    title_2: str = None
    image_2: str
    title_3: str = None
    image_3: str = None


class PassScheme(BaseModel):
    add_time: datetime
    beauty_title: str
    title: str
    other_titles: str = None
    connect: str = None
    status: str = "new"

    class Config:
        orm_mode = True
