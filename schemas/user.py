from pydantic import BaseModel

class User(BaseModel):
    id:int

class UserIn(User):
    name:str
    email:str
    upassword:str

