from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import *

trips = Table(
    "trips",
    meta,
    Column("trip_id", Integer, primary_key=True),
    Column("train_id", Integer,ForeignKey("trains.id")),
    Column("routeID", Integer,ForeignKey("routes.routeID")),
    Column("dt_departure",DateTime),
    Column("duration", DateTime),
    Column("dt_arrival",DateTime),
)
meta.create_all(engine)