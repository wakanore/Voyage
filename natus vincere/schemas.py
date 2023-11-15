from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel
@dataclass
class Hotel:
    id: int
    HotelName: str
    HotelDescription:str
    Image: str
    HotelType:str
    RoomCount: int
    FreeRooms: int

@dataclass
class Room:
    Image: str
    Type: str
    IsFree: bool
    MaxGuests:int
    BookingDate: str

@dataclass
class Owner:
    id: int
    firstname:str
    lastname: str
    emale: str
    password: str
    registerTime: str
    Hotels: Hotel

@dataclass
class Userr:
    id:int
    firstname: str
    lastname: str
    emale: str
    password: str
    registerTime: str
    currentHotel: Hotel




class User(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int


class UserCreate(BaseModel):
    password: str



