from fastapi import APIRouter, HTTPException
from config import db
from models.users import users
from schemas.user import User, UserCreate, UserLogin

auth_route = APIRouter()

@auth_route.post("/auth/login/", response_model=User, tags=["auth"])
def login(userLogin: UserLogin):
    user_db = db.engine.execute(users.select().where(users.c.email == userLogin.email)).first()
    userData = dict()
    if user_db:
        userData = {**user_db}
        if userLogin.password == userData["password"]:
            return userData

        else:
            raise HTTPException(status_code=201,detail="password is wrong")
            
    raise HTTPException(status_code=400, detail= "user not found")


@auth_route.post("/auth/register", tags=["auth"], response_model=User)
def register(user:UserCreate):
    user_db = db.engine.execute(users.select().where(users.c.email == user.email)).first()

    if not user_db:
        id = db.engine.execute(users.insert().values(name=user.name, password=user.password, phone=user.phone, email=user.email)).lastrowid
        return db.engine.execute(users.select().where(users.c.id == id)).first()
    
    raise HTTPException(status_code=400, detail="user already exists")


@auth_route.delete("/auth/delete-user/{user_id}", tags=["auth"])
def delete_user(user_id:int):
    user_db = db.engine.execute(users.select().where(users.c.id == user_id))
    if user_db:
        return db.engine.execute(users.delete().where(users.c.id == user_id))

    raise HTTPException(status_code=400, detail="User not found")
