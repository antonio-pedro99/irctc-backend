from config.db import meta, engine
from sqlalchemy import Table, Column, PrimaryKeyConstraint, ForeignKey, Constraint
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import relationship

seats = Table(
    "seats",
    meta,
    Column("seat_number", Integer),
    Column("train_id", Integer, ForeignKey("trains.id")),
    Column("s_status",Boolean,default="False"),
    Constraint("train")
)
meta.create_all(engine)