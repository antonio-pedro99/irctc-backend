import email
from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    name: str
    email:str
    phone:str



# Properties to receive on item creation
class UserCreate(UserBase):
    passord:str
    

# Properties to receive on item update
class UserUpdate(UserBase):
    pass


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    age:int
    password:str
    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass
