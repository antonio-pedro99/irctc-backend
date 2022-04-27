from typing import Optional
from pydantic import BaseModel
from schemas.trips import Trip


# Shared properties
class TicketBase(BaseModel):
    trip_id:int
    ticket_id: int
   
# Properties to receive on item creation
class TicketCreate(TicketBase):    
    payment_id:int


class TicketUpdate(TicketBase):
    passenger_id:int

# Properties shared by models stored in DB
class TicketInDBBase(TicketBase):
    passenger_id: int
    seat_number:int
    class Config:
        orm_mode = True


# Properties to return to client
class Ticket(TicketInDBBase):
    trip: Trip
    pass


