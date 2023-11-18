from sqlalchemy.orm import Session
from typing import List, Annotated
from fastapi import APIRouter, Depends
from user import register
import schemas
from fastapi import FastAPI, APIRouter, Path
from schemas import  User
from fastapi import HTTPException

user_router = APIRouter(prefix = '/users', tags = ['Пользователи'])
users =[]

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def get_users(db: Session):
    return db.query(schemas.User).offset(skip).limit(limit).all()



@user_router.get("/read_users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users



@user_router.post('/add_user/', name = 'add_user', response_model=User)
def add_user(user: User):
    users.append(user)
    return user

@user_router.get('/get_user_by_id/', name = 'get_user_by_id', response_model = User)
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')

@user_router.get('/get_user_by_username/', name = 'get_user_by_username', response_model = User)
def get_user_by_username(username: str):
    for user in users:
        if user.username == username:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')

@user_router.get('/get_user_by_email/', name = 'get_user_by_email', response_model = User)
def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    raise HTTPException(status_code = 404, detail = 'user not found')



@user_router.post("/register_user/", response_model=schemas.User, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)



