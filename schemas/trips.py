from typing import Optional, List
from pydantic import BaseModel
from schemas.route import Route


# Shared properties
class TripBase(BaseModel):
    dt_departure: str
    dt_arrival: str
    


# Properties to receive on item creation
class TripCreate(TripBase):
    train_id: int
    route_id:int
   

# Properties to receive on item update
class TripUpdate(TripBase):
    route:List[str]
    stops:List[str]

# Properties shared by models stored in DB
class TripInDBBase(TripBase):
    trip_id: int
    train_id:int
    route_id:int
    duration: int
    class Config:
        orm_mode = True


class Stop(TripInDBBase):
  pass
# Properties to return to client
class Trip(TripInDBBase):
    routes: List[Route]
    stops:List[Stop]
    pass


# Properties properties stored in DB
class ItemInDB(TripInDBBase):
    pass
