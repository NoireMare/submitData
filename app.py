
from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

import schemas
from database.models import Base
from database.database import engine, SessionLocal
from sqlalchemy.orm import Session
from database import crud


Base.metadata.create_all(bind=engine)

api = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.post("/new_pass/create", status_code=201)
def submitData(pass_: schemas.Pass, user: schemas.User, level: schemas.Level, image: schemas.Image,
               coordinate: schemas.Coordinate, db: Session = Depends(get_db)):
    crud.CreatePass.create_user(db=db, user=user)
    crud.CreatePass.create_level(db=db, level=level)
    crud.CreatePass.create_images(db=db, image=image)
    crud.CreatePass.create_coordinate(db=db, coordinate=coordinate)
    new_pass = crud.CreatePass.create_pass(db=db, pass_=pass_)
    return JSONResponse({"status": 200, "message": "Отправлено успешно", "id": new_pass.id})





