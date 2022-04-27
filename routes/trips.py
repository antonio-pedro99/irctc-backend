from optparse import Option
from fastapi import APIRouter
from typing import List, Optional

import sqlalchemy
from schemas.query import SearchQueryBase
from schemas.train import *
from schemas.seat import Seat
from schemas.trips import Trip, TripCreate, TripUpdate
from utils.cruds import get_route_by_station, get_station_by_name
from utils.trips_crud import create_trip, get_seat_by_train_id, get_train_by_id, get_trip_admin, get_trip_by_id, update_trip_details
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
    query = text("""select * from 
        available_trips
            where 
        location_from = '{0}' and destination_to = '{1}'""".format(location, destination))
    return db.engine.execute(query).all()


@trip_route.put("/trips/{id}", tags=["admin/Trip"])
def update_trip(trip:TripUpdate, id:int):
    update_trip_details(id=id,trip=trip )
    return get_trip_by_id(id=id)

@trip_route.get("admin/trips", tags=["admin/Trip"])
def get_trips(location_from:Optional[str], location_to:str):
   return get_trip_admin(location_from=location_from, location_to=location_to)


@trip_route.post("/trips/new", tags=["admin/Trip"])
def create_new_trip(trip:TripCreate):
   return create_trip(trip=trip)