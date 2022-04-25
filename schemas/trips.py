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
    route:List[Route]
    stops:List[Stop]

# Properties properties stored in DB
class ItemInDB(TripInDBBase):
    pass
