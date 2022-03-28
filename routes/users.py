from fastapi import APIRouter
from config import db
from models.users import users
from schemas.user import UserIn

user_route = APIRouter()
@user_route.get("/users")
def get_users():
    return db.engine.execute("select * from users").all()

@user_route.get("/users/{id}", response_model=UserIn)
def get_user(id:int):
    return db.engine.execute(users.select().where(users.c.id == id)).first()

@user_route.post("/users/")
def create_user(user:UserIn):
    return {"hello":"wrld"}