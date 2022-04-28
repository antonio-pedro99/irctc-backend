## creating all triggers


DELIMITER //
	create trigger update_trip_duration after insert on trips for each row
    begin
		declare duration int;
        declare tmp int;
        declare _duration varchar(8);
        declare _minute int;
        set tmp =  (datediff(hour, New.dt_departure, New.dt_arrival));
        
        if tmp = 0 then
			set _duration =  (timestampdiff(minute, New.dt_departure, New.dt_arrival));
		else 
			set _duration = tmp;
		end if;
        
        update trips set duration = _duration where trip_id = New.trip_id;
    end;
//


drop trigger if exists after_update_trip;
delimiter //
create trigger after_update_trip
after update on railway_system.trips for each row
 begin
	declare msg varchar(255);
    declare _type varchar(50);
    declare title varchar(100);
    declare date_now datetime;
    
    set date_now = (select Now());
    if OLD.routeID != New.routeID then
		set title = concat("Trip update: Route has changed");
		set msg = concat("Your trip with ID  ", Old.trip_id, " has changed its route.");
	elseif Old.dt_departure != New.dt_departure then
		set title = concat("Trip update: schedule has been changed.");
		set msg = concat("Your trip with ID  ", Old.trip_id, " has changed the departure schedule from ", OLD.dt_departure, " to", New.dt_departure);
	elseif old.train_id != New.train_id then
		set title = concat("Trip update: Train has changed");
		set msg = concat("Your trip with ID  ", Old.trip_id, " has changed the train ", OLD.train_id, " to.", New.train_id);
	elseif old.dt_arrival != new.dt_arrival then
		if datediff(old.dt_arrival, old.dt_departure) > datediff(new.dt_arrival, old.dt_departure) then
			set title = concat("Trip update: Ups! your trip might delay");
			set msg = concat("It seems that your trip ", Old.trip_id, ",  is going to delay for ", datediff(old.dt_arrival, new.dt_departure), " days.");
		else 
			set title = concat("Trip update: Wow, your trip is arriving early.");
			set msg = concat("It seems that your trip ", Old.trip_id, ",  is going to arrive early. It will take now ", datediff(new.dt_arrival, old.dt_departure), " days.");
		end if;
	end if;
	insert into railway_system.notification_template(title, sourceId, createdAt, content) values(title, Old.trip_id, date_now, msg);    
 end //
 
 
 

 delimiter //
create trigger after_insert_ticket
after insert on tickets for each row 
 begin
	declare msg varchar(255);
    declare _type varchar(50);
    declare title varchar(100);
    declare date_now datetime;
    
    set date_now = (select Now());
	set msg = "You have just received a new booking.";
    set title = "New booking";
    
	insert into railway_system.notification_template(title, sourceId, createdAt, content)  values(title, New.ticket_id, date_now, msg);
 end //


 