from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import database
from routes.passengers import passenger_route
from routes.auth import auth_route
from routes.users import user_route
from routes.trips import trip_route
from routes.tickets import ticket_route
from routes.razor_pay import razor_pay_api_fake
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods = ["*"],
    allow_origins = ["*"]
)

app.include_router(passenger_route)
app.include_router(user_route)
app.include_router(auth_route)
app.include_router(trip_route)
app.include_router(ticket_route)
app.include_router(razor_pay_api_fake)

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdwon():
    pass
