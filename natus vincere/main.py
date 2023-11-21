from typing import List
from dataclasses import dataclass

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import FastAPI, APIRouter, Path
from user_router import user_router
from hotel import hotel_router

app = FastAPI()


app.include_router(user_router)

app.include_router(hotel_router)

