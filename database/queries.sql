use railway_system;

SELECT 
    @jj:=seat_number
FROM
    seats AS S
WHERE
    S.s_status = 0
        AND S.train_id IN (SELECT 
            T.train_id
        FROM
            trips AS T
            
        WHERE
            T.trip_id = trip_id)
LIMIT 1;

INSERT into tickets(payment_id, passenger_id , trip_id, seat_number) values
            (payment_id, passenger_id,trip_id,@jj);


select * from trains as T where id in (select S.train_id from trips  as S where S.trip_id = 4);
select * from seats;
#
select * from seats where train_id;
select * from trips;
select * from routes;
select * from trips as T1 inner join trips as T2 on ();


insert into routes(location, final_destination, price) values(96, 11, 100), (1, 50, 200);

SELECT 
    *
FROM
    routes AS R1
        INNER JOIN
    routes AS R2 ON R1.location = R2.final_destination;


select * from stations where city = "Gurgaon";
select * from routes;
select * from trips;

select * from available_trips;


Select R1.routeID from routes R
inner join routes R1
on R.final_destination = R1.location
where R.location = 11 and R1.final_destination = 14;

select T.routeID from trips as T
where T.routeID in (Select R.routeID from routes R
inner join routes R1
on R.final_destination = R1.location
where R.location = 11 and R1.final_destination = 14) or T.routeID in (Select R1.routeID from routes R
inner join routes R1
on R.final_destination = R1.location
where R.location = 11 and R1.final_destination = 14);



#create trip: location, final_destination


select * from stations;

SELECT 
    *
FROM
    trips AS T1
        INNER JOIN
    trips AS T2 ON T1.routeID IN (SELECT 
            routeID
        FROM
            routes AS R1
        WHERE
            R1.location IN (SELECT 
                    id
                FROM
                    stations AS S1
                WHERE
                    S1.city = 'Gurgaon')
                AND R1.final_destination IN (SELECT 
                    id
                FROM
                    stations AS S1
                WHERE
                    S1.city = 'Shimla'))
		and T2.routeID in (
        select routeId from routes as R2 where R2.location in (select id from stations as S2 where S2.city = "Shimla"))
        AND T1.train_id IN (SELECT 
            train_id
        FROM
            seats AS S1
        WHERE
            S1.s_status = 0) 
		And T2.train_id in (select train_id from seats as S2 where S2.s_status = 0);
        
        




select  * from trips as T1
WHERE
    T1.routeID IN (SELECT 
            routeID
        FROM
            routes AS R1
        WHERE
            R1.location IN (SELECT 
                    id
                FROM
                    stations AS S1
                WHERE
                    S1.city = 'Gurgaon')
                AND R1.final_destination IN (SELECT 
                    id
                FROM
                    stations AS S1
                WHERE
                    S1.city = 'Shimla'))
        AND T1.train_id IN (SELECT 
            train_id
        FROM
            seats AS S1
        WHERE
            S1.s_status = 0);




