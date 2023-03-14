from datetime import datetime
from typing import Optional
from venv import create
from fastapi import HTTPException
from sqlalchemy import text
from config import db
from models.trains import trains
from models.seats import seats
from models.trips import trips
from models.routes import routes
from models.stations import stations
from schemas.trips import TripCreate, TripUpdate
from utils.cruds import create_route, get_route_by_station, get_station_by_name

def get_seat_by_train_id(id):
    query = text("select * from trains where id = '{0}'".format(id))
    return db.engine.execute(query).all()

def get_train_by_id(id):
    query = text("select * from trains where id = '{0}'".format(id))
    return db.engine.execute(query).first()

def get_trip_by_id(id):
    query = text("select * from trips where trip_id = '{0}'".format(id))
    return db.engine.execute(query).first()

def get_route_by_id(id):
    query = text("select * from routes where routeID = '{0}'".format(id))
    return db.engine.execute(query).first()


def get_trip_by_route_id(id:int):
    query = text("select * from trips where routeID = '{0}'".format(id))
    return db.engine.execute(query).first()

def get_station_by_id(id):
    query = text("select * from stations where id = '{0}'".format(id))
    return db.engine.execute(query).first()

def create_trip(trip:TripCreate):
    route_db = get_route_by_station(location_name=trip.location_station, location_city=trip.location_city, final_destination_city=trip.final_destination_city, final_destination_name=trip.final_destination_station)
    if route_db:
            trip_ = get_trip_by_route_id(route_db)
            if trip_:
                trip_db = {**trip_}
                if trip_db["dt_departure"] != trip.dt_departure:
                    inserted = db.engine.execute(trips.insert().values(train_id = trip.train_id, routeID= route_db, dt_departure= trip.dt_departure, dt_arrival= trip.dt_arrival)).lastrowid
                    return get_trip_by_id(id=inserted)
         
    raise HTTPException(status_code=400, detail="can not add this trip")


def get_trip_admin(location_from:str, location_to:str):
    query = text("""
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

def update_trip_details(id:int, trip:TripUpdate):
    trip_db = get_trip_by_id(id=id)
    queries = []
    if trip_db:
        if trip.train_id:
            queries.append(text("update trips set train_id = '{0}' where trip_id = '{1}'".format(trip.train_id, id)))
        elif trip.dt_departure:
            queries.append(text("update trips set dt_departure = '{0}' where trip_id = '{1}'".format(trip.dt_departure, id)))
        elif trip.dt_arrival:
            queries.append(text("update trips set dt_arrival = '{0}' where trip_id = '{1}'".format(trip.dt_arrival,id)))
        elif trip.route_id:
            queries.append( text("update trips set route_id = '{0}' where trip_id = '{1}'".format(trip.route_id, id)))
        for query in queries:
            db.engine.execute(query)
