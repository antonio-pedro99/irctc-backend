import datetime
from typing import Optional, List
from pydantic import BaseModel
from schemas.route import Route


# Shared properties
class TripBase(BaseModel):
    dt_departure: Optional[str] = datetime.datetime.now()
    dt_arrival: Optional[str]
    


# Properties to receive on item creation
class TripCreate(TripBase):
    train_id: int
    location_city:str
    location_station:str
    final_destination_city:str
    final_destination_station:str

    
   
# Properties shared by models stored in DB
class TripInDBBase(TripBase):
    trip_id: int
    train_id:int
    route_id:int
    duration: Optional[int]
    class Config:
        orm_mode = True


class Stop(TripInDBBase):
  pass
# Properties to return to client
class Trip(TripInDBBase):
    routes: List[Route]
   # stops:List[Stop]

# Properties to receive on item update
class TripUpdate(TripBase):
    train_id: Optional[int]
    route_id:Optional[int]

# Properties properties stored in DB
class ItemInDB(TripInDBBase):
    pass
