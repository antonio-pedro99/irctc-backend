from calendar import c
from config import db
from models.trains import trains
from models.seats import seats
from models.trips import trips
from models.routes import routes
from models.stations import stations

def get_seat_by_train_id(id):
    return db.engine.execute(seats.select().where(seats.c.train_id  == id)).all()

def get_train_by_id(id):
    return db.engine.execute(trains.select().where(trains.c.id == id)).first()

def get_trip_by_id(id):
    return db.engine.execute(trips.select().where(trips.c.trip_id == id)).first()

def get_route_by_id(id):
    return db.engine.execute(routes.select().where(routes.routeID == id)).first()

def get_station_by_id(id):
    return db.engine.execute(stations.select().where(stations.c.id == id))

def create_trip():
    pass

def update_trip(id:int):
    pass
