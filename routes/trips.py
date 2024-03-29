from optparse import Option
from fastapi import APIRouter
from typing import List, Optional

import sqlalchemy
from schemas.query import SearchQueryBase
from schemas.route import RouteCreate
from schemas.train import *
from schemas.seat import Seat
from schemas.trips import Trip, TripCreate, TripUpdate
from utils.cruds import create_route, get_route_by_station, get_station_by_name, update_route
from utils.trips_crud import create_trip, get_seat_by_train_id, get_train_by_id, get_trip_admin, get_trip_by_id, update_trip_details
from config import db
from sqlalchemy import text

trip_route = APIRouter()

@trip_route.get("/seats/{train_id}", response_model=List[Seat], tags=["Trip"])
def get_seats(id:int):
    return get_seat_by_train_id(id=id)


@trip_route.get("/trips/all", tags=["admin/Trip"])
def get_all():
    query = text("select * from available_trips_admin")
    return db.engine.execute(query).all()

@trip_route.get("/trips/all_from_current_location/{current_location}", tags=["Trip"])
def get_trip_by_current_location(current_location:str):
    query = text("""select * from available_trips where
            location_from = '{0}'""".format(current_location))
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
def get_trip_by_location_to_destination(location:Optional[str], destination:Optional[str]):
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

@trip_route.post("/admin/routes", tags=["admin/Trip"])
def create_new_route(route:RouteCreate):
    return create_route(route.location, route.final_destination, route.price)
    
@trip_route.post("/trips/new", tags=["admin/Trip"])
def create_new_trip(trip:TripCreate):
   return create_trip(trip=trip)

@trip_route.put("/trips/routes/{id}/update", tags=["admin/Trip"])
def create_update_trip_price(id:int, price:float):
   return update_route(id=id, price=price)

@trip_route.delete("/trips/routes/{id}/delete", tags=["admin/Trip"])
def delete_route(id:int):
   return  delete_route(id=id)