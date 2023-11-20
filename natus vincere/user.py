from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST
from db import Base
from model import User
import datetime

import random
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

def register(db: Session, user_data: User):
    unique_sequence = uniqueid()
    if db.scalar(select(User).where(User.email == user_data.email)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User with this email already exists!"
        )
    user = User(
        id=user_data.unique_sequence,
        username=user_data.username,
        email=user_data.email,
        Image=user_data.Image,
        type=user_data.type,
        age=user_data.age,
        registrationTime=user_data.registrationTime,
    )
    user.password = user_data.password
    db.add(user)
    db.commit()
    return {
        "id": user.id,
        "email": user.email,
        "id": user.id,
        "username": user.username,
        "emale": user.emale,
        "Image": user.Image,
        "type" : user.type,
        "age": user.age,
        "registrationTime": user.registrationTime
    }

async def create_user(db: Session, user: User):
    query = user.insert().values(
        username=user.username,
        email=user.email,
        Image=user.Image,
        type=user.type,
        age=user.age,
    )
    user_id = await Base.execute(query)
    registrationTime = await Base.execute(datetime.datetime.now())

    return {**user.dict(), "id": user_id, "register_time": registrationTime}
