from sqlalchemy import text
from config import db
from models.stations import stations


def get_station_by_name(name:str, city:str):
    query = text("select * from stations where name = '{0}' and city = '{1}'".format(name, city))
    return db.engine.execute(query).first()
  

def get_route_by_station(location_name:str, location_city:str, final_destination_name:str,final_destination_city):
    q = text("""
SELECT 
    routeID
FROM
    routes AS R
        INNER JOIN
    stations AS S1 ON R.location = S1.id
        INNER JOIN
    stations AS S2 ON R.final_destination = S2.id
WHERE
    S1.name = '{0}'
        AND S1.city = '{1}'
	and
    S2.name = '{2}' and S2.city = '{3}'""""".format(location_name, location_city, final_destination_name, final_destination_city))

    return db.engine.execute(q).first()