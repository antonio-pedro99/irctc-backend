from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import *

routes = Table(
    "routes",
    meta,
    Column("routeID", Integer, primary_key=True),
    Column("location", ForeignKey("stations.id")),
    Column("final_destination", ForeignKey("stations.id")),
)
meta.create_all(engine)