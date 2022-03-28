from tkinter import DoubleVar
from fastapi import FastAPI
from config.db import database
from config import db
from routes.passengers import passenger_route
from routes.users import user_route
from models.users import users

app = FastAPI()

app.include_router(passenger_route)
app.include_router(user_route)

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdwon():
    pass

