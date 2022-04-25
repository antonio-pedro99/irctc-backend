
from fastapi import APIRouter, HTTPException
from config import db
from models.users import users

from typing import List
from models.tickets import tickets

from schemas.tickets import Ticket, TicketCreate
from schemas.user import  *
from schemas.train import *
from schemas.seat import Seat


user_route = APIRouter()

@user_route.get("/users")
def get_users():
    return db.engine.execute(users.select()).all()


@user_route.get("/users/{id}", response_model=User)
def get_user(id:int):
    return db.engine.execute(users.select().where(users.c.id == id)).first()


@user_route.get("/tickets/")
def create_user():
   
    _tickets = []
    for ticket in db.engine.execute(tickets.select()).all():
        ticket_json = dict()
        ticket_json["ticket_id"] = ticket[0]
        ticket_json["payment_id"] = ticket[1]
        ticket_json["passenger_id"] = ticket[2]
        ticket_json["trip_id"] = ticket[3]
        ticket_json["seat_number"] = ticket[4]
        
        for trip in db.engine.execute(tickets.select().where(tickets.c.trip_id == ticket[3])):
            print(trip)
        _tickets.append(ticket_json)
    return _tickets