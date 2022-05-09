from sqlalchemy import text
from fastapi import APIRouter, HTTPException
from config import db
from config.security import hash_password, verify_pwd
from models.users import users
from schemas.user import User, UserCreate, UserLogin

auth_route = APIRouter()

@auth_route.post("/auth/login/", response_model=User, tags=["auth"])
def login(userLogin: UserLogin):
    user_db = db.engine.execute("""select * from users where email = '{0}'""".format(userLogin.email)).first()
    userData = dict()
    if user_db:
        userData = {**user_db}
       
        if verify_pwd(userLogin.password, userData["password"]):
            return userData
        else:
            raise HTTPException(status_code=201,detail="password is wrong")

    raise HTTPException(status_code=400, detail= "user not found")


@auth_route.post("/auth/register", tags=["auth"])
def register(user:UserCreate):
    user_db = db.engine.execute(text("""select * from users where email = '{0}'""".format(user.email))).first()
    
    response = {
        "sucess":0,
    }

    if not user_db:
        hashed_password = hash_password(user.password)

        data = {
            "name": user.name,
            "password": hashed_password,
            "phone":user.phone,
            "email":user.email,
        }

        query = text("""
            insert into users(name,email,phone,password) values(:name,:email, :phone,:password)
        """)

        return db.engine.execute(query, **data).lastrowid
        
    response["sucess"] = 0
    raise HTTPException(status_code=400, detail="user already exists")


@auth_route.delete("/auth/delete-user/{user_id}", tags=["auth"])
def delete_user(user_id:int):
    user_db = db.engine.execute(text("""select * from users where id = '{0}'""".format(user_id))).first()
    if user_db:
        return db.engine.execute(text("""delete from users where id = '{0}'""".format(user_id)))

    raise HTTPException(status_code=400, detail="User not found")
