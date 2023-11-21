from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select
import schemas
from fastapi import FastAPI, APIRouter, Path
from schemas import  Hotel
from fastapi import HTTPException
from db import engine

hotel_router = APIRouter(prefix = '/hotels', tags = ['Отели'])

hotels =[]

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def get_hotel(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.Hotel).offset(skip).limit(limit).all()


@hotel_router.get("/read_hotel/", response_model=List[schemas.Hotel])
def read_hotel(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hotels = get_hotel(db, skip=skip, limit=limit)
    return hotels

@hotel_router.get('/get_hotel_by_id/', name = 'get_hotel_by_id', response_model = Hotel)
def get_hotel_by_id(hotel_id: int):
    for hotel in hotels:
        if hotel.id == hotel_id:
            return hotel
    raise HTTPException(status_code = 404, detail = 'hotel not found')

@hotel_router.get('/get_hotel_by_hotelname/', name = 'get_hotel_by_hotelname', response_model = Hotel)
def get_hotel_by_name (HotelName: str):
    sel = select([Hotel]).where(Hotel.c.name.like("%{HotelName}%".format(name=HotelName)))
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()

@hotel_router.post('/add_hotel/', name = 'add_hotel', response_model=Hotel)
def add_hotel(hotel: Hotel):
    hotels.append(hotel)
    return hotels
