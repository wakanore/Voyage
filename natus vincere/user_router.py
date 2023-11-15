from typing import List
from fastapi import APIRouter, Depends
from user import register
#from models.database import get_db

from dataclasses import dataclass

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
import schemas
from fastapi import FastAPI, APIRouter, Path
from schemas import Userr, User

user_router = APIRouter(prefix = '/users', tags = ['Пользователи'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.get('/', name = 'Вce пользователи', response_model = List[Userr])
def get_all_users():
    return users

@user_router.post('/', name = 'добавить пользователя', response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@user_router.get('/{user_id}', name = 'Получить пользователя', response_model = User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')

@user_router.post("", response_model=schemas.User, status_code=201)
def register_user(user_data: schemas.UserCreate):
    return register(db=db, user_data=user_data)




