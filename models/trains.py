from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import *

trains = Table(
    "trains",
    meta,
    Column("id", Integer, primary_key=True),
    Column("driver", String(255)),
    Column("seats", Integer),
)
meta.create_all(engine)