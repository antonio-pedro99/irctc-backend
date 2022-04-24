from typing import Optional, List
from pydantic import BaseModel

# Shared properties
class StationBase(BaseModel):
    city: str
    name: str
    code:str
    
    
# Properties to receive on item creation
class StationCreate(StationBase):
    pass
   
# Properties to receive on item update
class StationUpdate(StationBase):
    pass

# Properties shared by models stored in DB
class StationInDBBase(StationBase):
    id: int   
    class Config:
        orm_mode = True

# Properties to return to client
class Station(StationInDBBase):
    pass

