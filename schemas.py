from pydantic import BaseModel, validator, constr
from datetime import datetime


class BaseException(Exception):
    pass


class User(BaseModel):
    fam: str
    name: str
    otc: str = None
    phone: str = None
    email: str

    @validator('email')
    def validate_email(cls, value):
        if "@" and "." not in value:
            raise BaseException('The email is wrong')
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
    #user_id: User
    #coordinates: Coordinate
    #levels: Level
    #images: List[Image] = None
    #activities: List[PerevalActivities] = None

    class Config:
        orm_mode = True