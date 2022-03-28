from fastapi import APIRouter
from config import db


passenger_route = APIRouter()


@passenger_route.get("/passengers")
def get_passengers():
    return db.engine.execute("select * from passengers").all()