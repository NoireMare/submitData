from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class Pass(Base):
    __tablename__ = "passes"

    id = Column(Integer, primary_key=True, index=True)
    add_time = Column(DateTime, default=datetime.utcnow())
    beauty_title = Column(String(25), nullable=False)
    title = Column(String(25), unique=True, index=True, nullable=False)
    other_titles = Column(String(25), unique=True)
    connect = Column(String(35))
    status = Column(String(10), default='new')
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    level_id = Column(Integer, ForeignKey('levels.id', ondelete='CASCADE'))
    images_id = Column(Integer, ForeignKey('images.id', ondelete='CASCADE'))
    coordinates_id = Column(Integer, ForeignKey('coordinates.id', ondelete='CASCADE'))
    pass_creator = relationship('User', back_populates="passes")
    pass_levels = relationship("Level", back_populates="levels")
    pass_images = relationship("Image", back_populates="images")
    pass_coordinates = relationship("Coordinate", back_populates="coordinates")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fam = Column(String(25), nullable=False, index=True)
    name = Column(String(25), nullable=False, index=True)
    otc = Column(String(25))
    phone = Column(String(12))
    email = Column(String(25), index=True, nullable=False)
    passes = relationship('Pass', back_populates="pass_creator",
                          cascade='save-update, merge, delete',
                          passive_deletes=True
                          )


class Coordinate(Base):
    __tablename__ = "coordinates"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    height = Column(Integer, nullable=False)
    coordinates = relationship('Pass', back_populates="pass_coordinates",
                               cascade='save-update, merge, delete',
                               passive_deletes=True
                               )


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True, index=True)
    winter = Column(String(5), default="")
    summer = Column(String(5), default="")
    autumn = Column(String(5), default="")
    spring = Column(String(5), default="")
    levels = relationship('Pass', back_populates="pass_levels",
                          cascade='save-update, merge, delete',
                          passive_deletes=True
                          )


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    title_1 = Column(String(25), default="")
    image_1 = Column(String, nullable=False)
    title_2 = Column(String(25), default="")
    image_2 = Column(String, nullable=False)
    title_3 = Column(String(25), default="")
    image_3 = Column(String, default="")
    images = relationship('Pass', back_populates="pass_images",
                          cascade='save-update, merge, delete',
                          passive_deletes=True
                          )







