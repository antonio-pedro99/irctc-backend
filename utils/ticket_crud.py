from this import d
from sqlalchemy import text
from config import db
from models.tickets import tickets
from schemas.tickets import TicketCreate
from utils.user_crud import get_user_tickets

def get_all_tickets():
    return db.engine.execute(tickets.select()).all()

def get_ticket_by_user_id(userID:int):
    return db.engine.execute(tickets.select().where(tickets.c.passenger_id == userID)).all()

def get_ticket_by_id(id:int):
    query =  query = text("select * from booked_tickets where ticket_id = '{0}'".format(id));
    return db.engine.execute(query).first()

def create_user_ticket(ticket:TicketCreate):

    select_seat = text("""SELECT 
    @jj:=seat_number as seat
        FROM
            seats AS S
        WHERE
            S.s_status = 0
        AND S.train_id IN (SELECT 
            T.train_id
            FROM
                trips AS T
            WHERE
                T.trip_id = '{0}')
            LIMIT 1""".format(ticket.trip_id))

    new_seat = db.engine.execute(select_seat).first()["seat"]

    update_seat = text(""" UPDATE seats
			SET s_status = 1
			WHERE train_id in (SELECT T.train_id FROM trips as T WHERE T.trip_id = '{0}') AND seat_number = '{1}'""".format(ticket.trip_id, new_seat))
    
    db.engine.execute(update_seat)

    db.engine.execute(tickets.insert().values(passenger_id=ticket.passenger_id, payment_id=ticket.payment_id, trip_id = ticket.trip_id, seat_number = new_seat))

    return get_user_tickets(id=ticket.passenger_id)[-1]

def cancel_ticket(passenger_id:int, trip_id:int):
    query = text("update tickets set t_status = 0 where passenger_id = '{0}' and trip_id = '{1}'".format(passenger_id, trip_id))
    return db.engine.execute(query)


