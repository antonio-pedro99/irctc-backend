from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import *

payments = Table(
    "payments",
    meta,
    Column("paymentID", Integer, primary_key=True),
    Column("p_methodID",String(255),ForeignKey("payment_methods.p_methodID")),
    Column("amount",Float),
    Column("date",)
)
meta.create_all(engine)