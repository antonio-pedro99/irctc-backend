from fastapi import APIRouter
from typing import List, Optional

import sqlalchemy
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


@trip_route.put("/trips/", tags=["Trip"])
def update_trip(trip:TripUpdate):
    return {**trip}

@trip_route.get("admin/trips", tags=["admin"])
def get_trips(location_from:Optional[str], location_to:str):

    #run raw sql queries with python varialble
    query = sqlalchemy.text("""
        SELECT
            *
        FROM
            trips AS T
        WHERE
            T.routeID IN (SELECT
                    routeID
                FROM
                    routes AS R
                WHERE
                    R.location IN (SELECT
                            id
                        FROM
                            stations AS S
                        WHERE
                            S.city = '{0}')
                        AND R.final_destination IN (SELECT
                            id
                        FROM
                            stations AS S
                        WHERE
                            S.city = '{1}'))
                AND T.train_id IN (SELECT
                    train_id
                FROM
                    seats AS S
                WHERE
                    S.s_status = 0);
                    
    """.format(location_from, location_to))
    return db.engine.execute(query).all()