from config.db import meta, engine
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *

passengers = Table(
    "passengers",
    Column("id", Integer, primary_key = True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("phone", String(255)),
    Column("age", Integer),
)
meta.create_all(engine)