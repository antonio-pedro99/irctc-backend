from config import db
from models.routes import routes

""" def get_all():
    return db.engine.execute(routes.select()).all()

def get_route_by_trip_id(trip_id:int):
    return db.engine.execute(routes.select().where(routes.c.trip_id == userID)).all()

def get_ticket_by_id(id:int):
    return db.engine.execute(tickets.select().where(tickets.c.ticket_id == id)).first()


def create_user_ticket(userID:int):
    pass
 """
