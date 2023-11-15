from typing import List
from dataclasses import dataclass

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import FastAPI, APIRouter, Path
from user_router import user_router

app = FastAPI()


app.include_router(user_router)
