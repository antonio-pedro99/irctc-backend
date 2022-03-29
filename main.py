from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.db import database
from config import db
from routes.passengers import passenger_route
from routes.users import user_route
from models.users import users

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods = ["*"],
    allow_origins = ["*"]
)

app.include_router(passenger_route)
app.include_router(user_route)


@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdwon():
    pass

if __name__ == "__main__":
    uvicorn.run(app, reload =True)