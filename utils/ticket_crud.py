from config import db
from models.trains import trains
from models.tickets import tickets

def get_all_tickets():
    return db.engine.execute(tickets.select()).all()

def get_ticket_by_user_id(userID:int):
    return db.engine.execute(tickets.select().where(tickets.c.passenger_id == userID)).all()

def get_ticket_by_id(id:int):
    return db.engine.execute(tickets.select().where(tickets.c.ticket_id == id)).first()


def create_user_ticket(userID:int):
    pass

