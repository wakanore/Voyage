from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String, unique=True, index=True)
    lastname = Column(String, unique=True, index=True)
    register_time = Column(String, unique=True, index=True)
    Hotel = Column(String, unique=True, index=True)
    password = Column(String)

    items = relationship("Hotel", back_populates="owner")
    tokens = relationship("Room", back_populates="user")

class Owner(Base):
    __tablename__ = "owner"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String, unique=True, index=True)
    lastname = Column(String, unique=True, index=True)
    register_time = Column(String, unique=True, index=True)
    Hotel = Column(String, unique=True, index=True)
    password = Column(String)

    items = relationship("Hotel", back_populates="owner")
    tokens = relationship("Room", back_populates="user")

class Room(Base):
    __tablename__ = "rooms"
    image = Column(String, unique=True, index=True)
    type_room = Column(String, unique=True, index=True)
    max_user = Column(Integer, primary_key=True, index=True)
    register_time = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="Room")

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    hotelname = Column(String, unique=True, index=True)
    hotel_discription = Column(String, unique=True, index=True)
    image = Column(String, unique=True, index=True)
    type_hotel = Column(String, unique=True, index=True)
    room_count = Column(Integer, primary_key=True, index=True)

    user = relationship("Owner", back_populates="Hotel")


