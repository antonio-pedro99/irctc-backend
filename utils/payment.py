from datetime import datetime
from sqlalchemy import text
from config import db
from models.stations import stations
from sqlalchemy import text

def create_payment(payment_method_id:int, amount:float):
    payment = {
        "p_methodID": payment_method_id,
        "amount": amount,
        "date": datetime.now()
    }
    
    q =  text("""insert into payments(p_methodID, amount, date) values(:p_methodID, :amount, :date)""")
    inserted =db.engine.execute(q, **payment).lastrowid

    return db.engine.execute("""
    SELECT 
    M.method AS channel, P.paymentID
FROM
    payment_methods AS M
        INNER JOIN
    payments AS P ON P.p_methodID = M.p_methodID and P.paymentID = '{0}'""".format(inserted)).first()


def get_payment_methods():
    return db.engine.execute(text("select * from payment_methods")).all()