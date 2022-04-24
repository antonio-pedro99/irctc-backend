from config.db import meta, engine
from sqlalchemy import Table, Column, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import *

payment_methods = Table(
    "payment_methods",
    meta,
    Column("p_methodID", Integer, primary_key=True),
    Column("method",String(255)),
    Column("s_status",Boolean,default="False"),
)
meta.create_all(engine)