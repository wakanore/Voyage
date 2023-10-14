from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


# Благодаря этой функции клиент видит ошибки, происходящие на сервере, вместо "Internal server error"
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

class Guest(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    password: str
    registerTime: str
    currentHotel: str

class Owner(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    password: str
    registerTime: str
    Hotels: str

class Hotel(BaseModel):
    id: int
    name: str
    hotelDiscription: str
    image: str
    hotelType: str
    roomCount: int
    FreeRooms: Room

class Room(BaseModel):
    image: str
    RoomType: str
    IsFree: bool
    MaxGuest: int
    bookingTime: str

@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"




