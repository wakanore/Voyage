from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

Guest = Table(
    "Guest",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("firstname", String, nullable=False),
    Column("lastname", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("password", String, nullable=False),
    Column("currentHotel", String, nullable=False),
)

Owner = Table(
    "Owner",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("firstname", String, nullable=False),
    Column("lastname", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("password", String, nullable=False),
    Column("Hotel", List , nullable=False),
)

Hotel = Table(
    "Hotel",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("Name", String, nullable=False),
    Column("HotelDescription", String, nullable=False),
    Column("Image", String, nullable=False),
    Column("HotelType", String, nullable=False),
    Column("RoomCount", Integer, primary_key=True),
    Column("FreeCount", Room, primary_key=True),
)

Hotel = Table(
    "Hotel",
    metadata,
    Column("Image", String, nullable=False),
    Column("RoomType", String, nullable=False),
    Column("MaxGuest", Integer, primary_key=True),
    Column("IsFree", Boolean, primary_key=True),
)
