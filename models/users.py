from config.db import meta, engine
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *

users = Table(
    "Users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("phone", String(255)),
    Column("age", Integer),
    Column("gender",String(6)),
    Column("upassword", String(255)),
)
meta.create_all(engine)