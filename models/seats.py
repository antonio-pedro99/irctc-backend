from config.db import meta, engine
from sqlalchemy import Table, Column, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import *

seats = Table(
    "seats",
    meta,
    Column("seat_number", Integer),
    Column("train_id", Integer),
    Column("s_status",Boolean,default="False"),
)
meta.create_all(engine)