from config.db import meta, engine
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *

stations = Table(
    "stations",
    meta,
    Column("id", Integer, primary_key=True),
    Column("city", String(255)),
    Column("name", String(255)),
    Column("code", String(5),unique=True),
)
meta.create_all(engine)