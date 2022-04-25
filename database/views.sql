use railway_system;

drop view if exists available_trips;
create  view available_trips as SELECT 
    LOCATION.city AS location_from,
    LOCATION.name AS local_metrostation,
    LOCATION.code AS location_code,
	DESTINATION.city AS destination_to,
    DESTINATION.name AS destination_metrostation,
    DESTINATION.code AS destination_code,
    R.price,
    TRIP.trip_id,
    TRIP.dt_departure,
    TRIP.duration,
    TRIP.train_id,
    TRIP.dt_arrival
FROM
    stations AS LOCATION
        INNER JOIN
    routes AS R ON LOCATION.id = R.location
        INNER JOIN
    trips AS TRIP ON TRIP.routeID = R.routeID
        INNER JOIN
    stations AS DESTINATION ON R.final_destination = DESTINATION.id
        AND DATEDIFF(TRIP.dt_departure, NOW()) >= 0;