from fastapi import APIRouter, Depends
from starlette import status
from .. import schemas, database
from sqlalchemy.orm import Session
from .. repository import user
router = APIRouter(prefix="/user",
tags=['users'])

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)
   

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return user.show(id,db)