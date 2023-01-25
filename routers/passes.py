from fastapi import Depends, status, HTTPException, APIRouter
from starlette.responses import JSONResponse

import schemas
from database.crud import PassCrud
from database.models import Pass, User

router = APIRouter(prefix='/passes', tags=['passes'])


class EditingIsProhibited(Exception):
    pass


@router.post("/create", status_code=status.HTTP_201_CREATED)
def submitData(pass_: schemas.PassScheme, user: schemas.UserScheme, level: schemas.LevelScheme,
               image: schemas.ImageScheme, coordinate: schemas.CoordinateScheme, db: PassCrud = Depends()):
    db.create_user(user=user)
    db.create_level(level=level)
    db.create_images(image=image)
    db.create_coordinate(coordinate=coordinate)
    new_pass = db.create_pass(pass_=pass_)
    return JSONResponse({"status": 201, "message": "New pass is created", "id": new_pass.id})


@router.get("/{pass_id}")
def get_pass_info(pass_id, db: PassCrud = Depends()):
    if db.session.query(Pass).filter(Pass.id == pass_id).first():
        pass_content = db.get_pass_info(pass_id=pass_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pass number {pass_id} doesn`t exist')
    return pass_content


@router.get("/user/{email}")
def get_passes_by_user_email(email, db: PassCrud = Depends()):
    if db.session.query(User).filter(User.email == email).first():
        return db.get_passes_by_user_email(email=email)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='User with such email doesn`t exist')


@router.patch("/{pass_id}/edit")
def change_pass_info(pass_id, pass_: schemas.PassScheme, level: schemas.LevelScheme, image: schemas.ImageScheme,
                     coordinate: schemas.CoordinateScheme, db: PassCrud = Depends()):
    pass_chosen = db.session.query(Pass).filter(Pass.id == pass_id).first()
    if pass_chosen:
        if pass_chosen.status.lower() == 'new':
            db.change_pass_info(pass_id=pass_id, pass_=pass_, level=level, image=image, coordinate=coordinate)
            return JSONResponse({'state': 1})
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={'state': 0, 'message': 'Pass`s status is not "new". Its info can`t be changed'}
            )
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail={'state': 0, 'message': "There is no such pass in the database"}
                            )
