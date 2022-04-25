from typing import List
from pydantic import BaseModel

from schemas.seat import Seat

# Shared properties
class TrainBase(BaseModel):
    driver:str
    seats:int

# Properties to receive on Train creation
class TrainCreate(TrainBase):
    pass

# Properties to receive on Train update
class TrainUpdate(TrainBase):
    pass

# Properties shared by models stored in DB
class TrainInDBBase(TrainBase):
    id:int
    class Config:
        orm_mode = True

# Properties to return to client
class Train(TrainInDBBase):
    seats: List[Seat] = []

# Properties properties stored in DB
class TrainInDB(TrainInDBBase):
    pass
