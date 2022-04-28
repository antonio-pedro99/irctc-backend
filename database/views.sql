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
    stations AS DESTINATION ON R.final_destination = DESTINATION.id;


drop view if exists unavailable_trips;
create  view unavailable_trips as SELECT 
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
    stations AS DESTINATION ON R.final_destination = DESTINATION.id;


drop view  if exists booked_tickets; 
CREATE VIEW booked_tickets AS
    SELECT 
        TICKET.passenger_id AS passenger_id,
        USER.name AS issued_by,
        TRIP.trip_id AS trip_id,
        TICKET.ticket_id AS ticket_id,
        TRIP.location_from AS location,
        TRIP.destination_to AS destination,
        TRIP.price AS price,
        TRIP.train_id AS trainId,
        TICKET.t_status AS status,
        TRIP.dt_departure AS departure,
        TRIP.dt_arrival AS arrival,
        TICKET.seat_number AS seat
    FROM
        unavailable_trips AS TRIP
            INNER JOIN
        tickets AS TICKET ON TICKET.trip_id = TRIP.trip_id
            INNER JOIN
        users AS USER ON passenger_id = USER.id
    ORDER BY ticket_id ;
    
    
drop view if exists notifications_view_user; 
 CREATE VIEW notifications_view_user AS
    SELECT 
        N.title AS title,
        N.sourceId AS `source`,
        N.createdAt AS `date`,
        N.content AS content,
        T.passenger_id
    FROM
        notification_template AS N
            INNER JOIN
        booked_tickets AS T ON T.trip_id = N.sourceId;

 drop view if exists notifications_view_station; 
 CREATE VIEW notifications_view_station AS
    SELECT 
        N.title AS title,
        N.sourceId AS `source`,
        N.createdAt AS `date`,
        N.content AS content,
        T.passenger_id
    FROM
        notification_template AS N
            INNER JOIN
        booked_tickets AS T ON T.trip_id = N.sourceId;
 