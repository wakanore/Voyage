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


@user_router.get('/', name = 'get_users_all', response_model = List[Userr])
def get_users_all():
    return users

@user_router.post('/', name = 'add_user', response_model=User)
def add_user(user: User):
    users.append(user)
    return user

@user_router.get('/{user_id}', name = 'get_user_by_id', response_model = User)
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')

@user_router.get('/{user_id}', name = 'get_user_by_username', response_model = User)
def get_user_by_username(username: str):
    for user in users:
        if user.username == username:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')

@user_router.get('/{user_id}', name = 'get_user_by_email', response_model = User)
def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')

@user_router.post("", response_model=schemas.User, status_code=201)
def register_user(user_data: schemas.UserCreate):
    return register(db=db, user_data=user_data)





