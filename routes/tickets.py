from typing import List
from fastapi import APIRouter
from config import db
from schemas.tickets import Ticket
from models.tickets import tickets
from utils.ticket_crud import *
from utils.trips_crud import get_route_by_id, get_trip_by_id

ticket_route = APIRouter()

@ticket_route.get("/admin/tickets/", response_model = List[Ticket], tags=["admin/tickets"])
def get_all():
    ticket_dict =dict()
    result = []
    """  for ticket in get_all_tickets():
        if ticket:
            ticket_db = get_ticket_by_id(ticket[0])
            ticket_dict = {**ticket_db}
            ticket_dict["trip"]  =  {**get_trip_by_id(ticket[3])} 
            ticket_dict["trip"]["routes"] = [].append(**get_route_by_id(ticket[]))
            ticket_dict["trip"]["price"] = 0
        result.append(ticket_dict)
    print(result) """
    return ""