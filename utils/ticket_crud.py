from sqlalchemy import text
from config import db
from models.tickets import tickets

def get_all_tickets():
    return db.engine.execute(tickets.select()).all()

def get_ticket_by_user_id(userID:int):
    return db.engine.execute(tickets.select().where(tickets.c.passenger_id == userID)).all()

def get_ticket_by_id(id:int):
    query =  query = text("select * from booked_tickets where ticket_id = '{0}'".format(id));
    return db.engine.execute(query).first()

def create_user_ticket(userID:int, trip_id:int, paymentid:int):
    pass

def cancel_ticket(passenger_id:int, trip_id:int):
    query = text("update tickets set t_status = 0 where passenger_id = '{0}' and trip_id = '{1}'".format(passenger_id, trip_id))
    return db.engine.execute(query)


