from fastapi import APIRouter, HTTPException
from typing import List
from schemas.user import  *
from schemas.train import *
from config import db

from utils.user_crud import get_all_users, get_details, get_notifications, get_user_by_id, get_user_tickets, update_user_details

user_route = APIRouter()

@user_route.get("/users", response_model = List[User], tags=["user"])
def get_users():
    return get_all_users()

@user_route.get("/users/{id}", response_model=User,  tags=["user"])
def get_user_by_his_id(id:int):
    return get_user_by_id(id)

@user_route.get("/users/{id}/tickets/", tags=["user"])
def get_tickets(id:int):
   return get_user_tickets(id=id)

@user_route.put("/users/{id}/update", tags=["user"])
def update_user(user:UserUpdate, id:int):
    update_user_details(user=user, id=id)
    return "updated"

@user_route.get("/users/{id}/details",  response_model = UserUpdate, tags=["user"])
def get_user_details(id:int):
    return get_details(id=id)

@user_route.get("/users/{id}/notifications", tags=["user"])
def get_nots(id:int):
    return get_notifications(id=id)
    