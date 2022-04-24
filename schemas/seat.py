from pydantic import BaseModel



# Shared properties
class SeatBase(BaseModel):
    seat_number:int
    train_id:int
    s_status:bool

# Properties to receive on Seat creation
class SeatCreate(SeatBase):
    pass

# Properties to receive on Seat update
class SeatUpdate(SeatBase):
    pass

# Properties shared by models stored in DB
class SeatInDBBase(SeatBase):
    pass
    class Config:
        orm_mode = True

# Properties to return to client
class Seat(SeatInDBBase):
    pass

# Properties properties stored in DB
class SeatInDB(SeatInDBBase):
    pass
