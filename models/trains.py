from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey, Constraint
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import relationship, RelationshipProperty

trains = Table(
    "trains",
    meta,
    Column("id", Integer, primary_key=True),
    Column("driver", String(255)),
    Column("seats", Integer, Constraint()),
    
)
meta.create_all(engine)