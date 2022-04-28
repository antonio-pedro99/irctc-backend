from traceback import print_exc
from typing import Optional
from sqlalchemy import text
from config import db
from models.stations import stations


def get_station_by_name(name:str, city:str):
    query = text("select * from stations where name = '{0}' and city = '{1}'".format(name, city))
    return db.engine.execute(query).first()

def get_route_by_station(location_name:str, location_city:str, final_destination_name:str,final_destination_city):
    q = text("""
SELECT 
    routeID
FROM
    routes AS R
        INNER JOIN
    stations AS S1 ON R.location = S1.id
        INNER JOIN
    stations AS S2 ON R.final_destination = S2.id
WHERE
    S1.name = '{0}'
        AND S1.city = '{1}'
	and
    S2.name = '{2}' and S2.city = '{3}'""""".format(location_name, location_city, final_destination_name, final_destination_city))

    return db.engine.execute(q).first()["routeID"]


def get_route_by_id(id:int):
    return db.engine.execute(text("select * from routes where routeID = '{0}'".format(id))).first()

def create_route(location:int, destination:int, price:float):
    query = text("select routeID from routes where location = '{0}' and final_destination ='{1}'".format(location, destination))
    route_db = db.engine.execute(query).first()

    if route_db:
        return {"error": "route already exists"}

    new_route = {
            "location": location,
            "final_destination": destination,
            "price": price
    }

    if price != 0:
        new_route["price"] = price
        query = text("""insert into routes(location, final_destination, price) values (:location, :final_destination, :price)""")
    else:
        new_route["price"] = 0
        query = text("""insert into routes(location, final_destination, price) values (:location, :final_destination, :price)""")
    id =  db.engine.execute(query, **new_route).lastrowid
    return get_route_by_id(id=id)

def update_route(routeID:int, price:float):
    pass
        