from config.db import meta, engine
from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import *

tickets = Table(
    "tickets",
    meta,
    Column("ticket_id", Integer, primary_key=True),
    Column("payment_id", Integer),
    Column("passenger_id", Integer,ForeignKey("Users.id")),
    Column("trip_id", Integer,ForeignKey("trips.trip_id")),
    Column("seat_number", Integer,ForeignKey("seats.id")),
)
meta.create_all(engine)