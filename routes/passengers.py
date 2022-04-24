from lib2to3.pgen2.token import OP
from typing import List, Optional
from fastapi import APIRouter
from config import db
import sqlalchemy
from schemas.passenger import *

passenger_route = APIRouter()

@passenger_route.get("/passengers",  response_model=List[Passenger])
def get_passengers():
    return db.engine.execute("select * from passengers").all()


@passenger_route.get("/trips")
def get_trips(location_from:str, location_to:Optional[str]):

    #run raw sql queries with python varialble
    query = sqlalchemy.text("""
        SELECT
            *
        FROM
            trips AS T
        WHERE
            T.routeID IN (SELECT
                    routeID
                FROM
                    routes AS R
                WHERE
                    R.location IN (SELECT
                            id
                        FROM
                            stations AS S
                        WHERE
                            S.city = '{0}')
                        AND R.final_destination IN (SELECT
                            id
                        FROM
                            stations AS S
                        WHERE
                            S.city = '{1}'))
                AND T.train_id IN (SELECT
                    train_id
                FROM
                    seats AS S
                WHERE
                    S.s_status = 0);
                    
    """.format(location_from, location_to))
    return db.engine.execute(query).all()