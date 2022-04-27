from lib2to3.pgen2.token import OP
from typing import List, Optional
from fastapi import APIRouter
from config import db
import sqlalchemy
from schemas.passenger import *

passenger_route = APIRouter()

@passenger_route.get("/passengers",  response_model=List[Passenger], tags=["passenger"])
def get_passengers():
    return db.engine.execute("select * from passengers").all()