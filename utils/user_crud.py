from this import d
from fastapi import Query
from config import db
from models.users import users
from sqlalchemy import text

from schemas.user import UserUpdate

def get_all_users():
    return db.engine.execute(users.select()).all();

def get_user_by_id(id:int):
    return db.engine.execute(users.select().where(users.c.id == id)).first()

def get_user_tickets(id:int):
    query = text("select * from booked_tickets where passenger_id = '{0}'".format(id))
    return db.engine.execute(query).all()

def get_user_by_email(email:str):
     return db.engine.execute(users.select().where(users.c.email == email)).first()

def get_details(id:int):
    return db.engine.execute(users.select().where(users.c.id == id)).first()


def update_user_details(user:UserUpdate, id:int):
    user_db = get_user_by_id(id=id)
    queries = []
    if user_db:
        if user.name:
            queries.append(text("update users set name = '{0}' where id = '{1}'".format(user.name, id)))
        elif user.email:
            queries.append(text("update users set email = '{0}' where id = '{1}'".format(user.email, id)))
        elif user.gender:
            queries.append(text("update users set gender = '{0}' where id = '{1}'".format(user.gender,id)))
        elif user.age:
            queries.append( text("update users set age = '{0}' where id = '{1}'".format(user.age, id)))
        for query in queries:
            db.engine.execute(query)
   # return db.engine.execute(users.select().where(users.c.id == id))

def get_notifications(id:int):
    query = text("select * from notifications_view_user where passenger_id = '{0}'".format(id))
    return db.engine.execute(query).all()

def read_notification(user_id:int, notification_id:int):
    pass

def delete_notification(user_id:int, notification_id:int):
    pass

