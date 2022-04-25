from fastapi import APIRouter
from typing import List
from schemas.train import *
from schemas.seat import Seat
from schemas.trips import Trip, TripUpdate
from utils.trips_crud import get_seat_by_train_id, get_train_by_id
from config import db
from sqlalchemy import text

trip_route = APIRouter()

@trip_route.get("/seats/{train_id}", response_model=List[Seat], tags=["Trip"])
def get_seats(id:int):
    return get_seat_by_train_id(id=id)


@trip_route.get("/trips/all", tags=["Trip"])
def get_all():
    query = text("select * from available_trips")
    return db.engine.execute(query).all()

@trip_route.get("/trips/{trip_id}")

@trip_route.get("/train/{id}", response_model=Train, tags=["Trip"])
def get_train(id:int):
    train = get_train_by_id(id=id)
    train_dict =dict()
    if train:
        seats  = get_seat_by_train_id(id=id)
        train_dict = {**train}
        train_dict["seats"] = seats
    return train_dict

@trip_route.get("/trips/{location}/to/{destination}", tags=["Trip"])
def get_trip_by_location_to_destionation(location:str, destination:str):
    query = text("select * from available_trips where location_from = '{0}' and destination_to = '{1}'".format(location, destination))
    return db.engine.execute(query).all()



@trip_route.put("/trips/", response_model=Trip, tags=["Trip"])
def update_trip(trip:TripUpdate):
    pass