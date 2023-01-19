from sqlalchemy.orm import Session
from database.models import User, Pass, Level, Image, Coordinate


class CreatePass:
    pass

    @staticmethod
    def create_user(user, db: Session):
        new_user = User(fam=user.fam, name=user.name, otc=user.otc, phone=user.phone, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def create_level(level, db: Session):
        new_level = Level(winter=level.winter, summer=level.summer, autumn=level.autumn, spring=level.spring)
        db.add(new_level)
        db.commit()
        db.refresh(new_level)
        return new_level

    @staticmethod
    def create_images(image, db: Session):
        new_image = Image(title_1=image.title_1, image_1=image.image_1, title_2=image.title_2,
                          image_2=image.image_2, title_3=image.title_3, image_3=image.image_3)
        db.add(new_image)
        db.commit()
        db.refresh(new_image)
        return new_image

    @staticmethod
    def create_coordinate(coordinate, db: Session):
        new_coordinate = Coordinate(longitude=coordinate.longitude, latitude=coordinate.latitude,
                                    height=coordinate.height)
        db.add(new_coordinate)
        db.commit()
        db.refresh(new_coordinate)
        return new_coordinate

    @staticmethod
    def create_pass(pass_, db: Session):
        new_pass = Pass(
            add_time=pass_.add_time, beauty_title=pass_.beauty_title,
            title=pass_.title, other_titles=pass_.other_titles, connect=pass_.connect,
            user_id=db.query(User).order_by(User.id)[-1].id,
            level_id=db.query(Level).order_by(Level.id)[-1].id,
            images_id=db.query(Image).order_by(Image.id)[-1].id,
            coordinates_id=db.query(Coordinate).order_by(Coordinate.id)[-1].id
        )
        db.add(new_pass)
        db.commit()
        db.refresh(new_pass)
        return new_pass


