from cgi import print_exception
from tokenize import Double
from typing import List, Optional
from pydantic import BaseModel
from schemas.station import Station


# Shared properties
class RouteBase(BaseModel):
    location:int
    final_destination:int
    price:float

# Properties to receive on Route creation
class RouteCreate(RouteBase):
    pass

# Properties to receive on Route update
class RouteUpdate(RouteBase):
    pass

# Properties shared by models stored in DB
class RouteInDBBase(RouteBase):
    routeID:int
    class Config:
        orm_mode = True


# Properties to return to client
class Route(RouteBase):
    location: Station
    final_destination:Station


# Properties properties stored in DB
class RouteInDB(RouteInDBBase):
    pass
