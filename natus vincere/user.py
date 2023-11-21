from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST
from db import Base
from schemas import User, UserCreate
import datetime

import random
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

def register(db: Session, user_data: User):
    if db.scalar(select(User).where(User.email == user_data.email)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User with this email already exists!"
        )
    user = User(email=user_data.email)
    db.add(user)
    db.commit()
    return {
        "id": user.id,
        "email": user.email,
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
