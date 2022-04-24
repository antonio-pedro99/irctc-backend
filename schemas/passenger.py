from pydantic import BaseModel
from typing import Optional

class Passenger(BaseModel):
    name:str
    email:str
    phone:str
    age:int


class PassengerCreate(Passenger):
    id:int
