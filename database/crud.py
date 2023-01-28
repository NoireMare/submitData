from sqlalchemy.orm import Session
from fastapi import Depends
from database.database import SessionLocal
from database.models import User, Pass, Level, Image, Coordinate


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PassCrud:
    def __init__(self, session: Session = Depends(get_db)) -> None:
        self.session = session

    def get_last_id(self, model) -> int:
        return self.session.query(model).order_by(model.id.desc()).first().id

    def create_user(self, user):
        new_user = User(**user.dict())
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def create_level(self, level):
        new_level = Level(**level.dict())
        self.session.add(new_level)
        self.session.commit()
        return new_level

    def create_images(self, image):
        new_image = Image(**image.dict())
        self.session.add(new_image)
        self.session.commit()
        return new_image

    def create_coordinate(self, coordinate):
        new_coordinate = Coordinate(**coordinate.dict())
        self.session.add(new_coordinate)
        self.session.commit()
        return new_coordinate

    def create_pass(self, pass_):
        new_pass = Pass(
            user_id=self.get_last_id(User), level_id=self.get_last_id(Level),
            images_id=self.get_last_id(Image), coordinates_id=self.get_last_id(Coordinate),
            **pass_.dict()
        )
        self.session.add(new_pass)
        self.session.commit()
        return new_pass

    def get_pass_info(self, pass_id: int):
        pass_ = self.session.query(Pass).filter(Pass.id == pass_id).first()
        return {'pass_': {'id': pass_.id, 'add_time': pass_.add_time, 'beauty_title': pass_.beauty_title,
                         'title': pass_.title, 'other_titles': pass_.other_titles, 'connect': pass_.connect,
                         'status': pass_.status},
                'coordinates': {'height': pass_.pass_coordinates.height, 'latitude': pass_.pass_coordinates.latitude,
                                'longitude': pass_.pass_coordinates.longitude
                                },
                'level': {'winter': pass_.pass_levels.winter, 'summer': pass_.pass_levels.summer,
                          'autumn': pass_.pass_levels.autumn, 'spring': pass_.pass_levels.spring
                          },
                'images': {'title_1': pass_.pass_images.title_1, 'title_2': pass_.pass_images.title_2,
                           'title_3': pass_.pass_images.title_3, 'image_1': pass_.pass_images.image_1,
                           'image_2': pass_.pass_images.image_2, 'image_3': pass_.pass_images.image_3
                           },
                'user': {'fam': pass_.pass_creator.fam, 'name': pass_.pass_creator.name, 'otc': pass_.pass_creator.otc,
                         'phone': pass_.pass_creator.phone, 'email': pass_.pass_creator.email
                         }
                }

    def get_passes_by_user_email(self, email: str):
        user_passes = []
        users = self.session.query(User).filter(User.email == email).all()
        for user in users:
            passes = self.session.query(Pass).filter(Pass.user_id == user.id).all()
            for pass_ in passes:
                pass_info = self.get_pass_info(pass_.id)
                del pass_info['user']
                user_passes.append(pass_info)
        return user_passes

    def change_pass_info(self, pass_id, pass_, level, image, coordinate):
        pass_to_change = self.session.query(Pass).filter(Pass.id == pass_id).first()
        for key, value in pass_:
            setattr(pass_to_change, key, value)
        level_to_change = self.session.query(Level).filter(Level.id == pass_to_change.level_id).first()
        for key, value in level:
            setattr(level_to_change, key, value)
        image_to_change = self.session.query(Image).filter(Image.id == pass_to_change.images_id).first()
        for key, value in image:
            setattr(image_to_change, key, value)
        coordinate_to_change = self.session.query(Coordinate).filter(Coordinate.id == pass_to_change.coordinates_id).first()
        for key, value in coordinate:
            setattr(coordinate_to_change, key, value)
        self.session.commit()
        return pass_to_change
