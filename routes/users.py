from turtle import update
from fastapi import APIRouter
from config import db
from models.users import users
from schemas.tickets import Ticket, TicketCreate
from schemas.user import UserCreate, UserUpdate, User
from schemas.user import  *
from schemas.train import Train, TrainCreate


user_route = APIRouter()
@user_route.get("/users")
def get_users():
    return db.engine.execute("select * from users").all()

@user_route.get("/users/{id}", response_model=User)
def get_user(id:int):
    return db.engine.execute(users.select().where(users.c.id == id)).first()

@user_route.post("/users/", response_model=Train)
def create_user(user: TrainCreate):
    return {"hello":""}