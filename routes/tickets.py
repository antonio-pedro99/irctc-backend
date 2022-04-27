from fastapi import HTTPException
from typing import List
from fastapi import APIRouter
from config import db
from schemas.tickets import Ticket, TicketUpdate
from models.tickets import tickets
from utils.ticket_crud import *
from sqlalchemy import text

from utils.trips_crud import get_trip_by_id
from utils.user_crud import get_user_by_id
ticket_route = APIRouter()

@ticket_route.get("/tickets/", tags=["tickets"])
def get_all_tickets():
    query = text("select * from booked_tickets")
    return db.engine.execute(query).all()

@ticket_route.get("/tickets/{id}", tags=["tickets"])
def get_by_id(id:int):
    return get_ticket_by_id(id)

@ticket_route.put("/tickets/cancel/", tags=["tickets"])
def user_cancel_ticker(ticket:TicketUpdate,):
    ticket_db = get_ticket_by_id(ticket.ticket_id)
    if ticket_db:
        if get_trip_by_id(ticket.trip_id) and get_user_by_id(ticket.passenger_id):
            cancel_ticket(ticket.passenger_id, ticket.trip_id)
            return ticket_db
    
    raise HTTPException(status_code=400, detail="unable to cancel ticket")