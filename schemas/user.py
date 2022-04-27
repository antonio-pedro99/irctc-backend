from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    email:Optional[str]
    phone:Optional[str]


class UserLogin(UserBase):
    password:str

# Properties to receive on item creation
class UserCreate(UserBase):
    name: str
    password:str
    

# Properties to receive on item update
class UserUpdate(UserBase):
    gender:Optional[str]
    name:Optional[str]
    age:Optional[str]
    


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    age:Optional[int]
    name: str
    password:str
    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserDetails(UserUpdate):
    pass
