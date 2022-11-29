drop database if exists irctc_db;
create database if not exists irctc_db;
use irctc_db;


## creating tables
CREATE TABLE passengers (
    `id` MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `gender` varchar(255) not null,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `phone` VARCHAR(10) NOT NULL UNIQUE,
    `age` MEDIUMINT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX(id, name),
    constraint chck_phone CHECK(phone REGEXP '^[0-9]+$'),
    constraint chck_dob CHECK(7<age<87)
)  AUTO_INCREMENT=1;




CREATE TABLE stations (
    `id` MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
    `city` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `code` VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (`id`),
    INDEX (id , city , code)
)  AUTO_INCREMENT=1;


CREATE TABLE `users` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `gender` varchar(255) not null default "male",
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `phone` VARCHAR(10) NOT NULL UNIQUE,
    `age` MEDIUMINT NULL,
	`password` varchar(255),
    constraint chck_phone1 CHECK(phone REGEXP '^[0-9]+$'),
    constraint chck_dob1 CHECK(7<age<87),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

CREATE TABLE trains (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `driver` varchar(255) not null,
  `seats` mediumint not null,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;


create table seats (
	seat_number  mediumint(8) NOT NULL,
    train_id mediumint(8) unsigned NOT NULL,
    s_status boolean not null default false,
    PRIMARY KEY(seat_number, train_id),
	INDEX `idx_seat` (s_status ASC, seat_number asc),
    FOREIGN KEY(train_id) REFERENCES trains(id)
);

create table routes (
	routeID  mediumint(8) NOT NULL auto_increment,
	location mediumint(8) unsigned NOT NULL,
    final_destination mediumint(8) unsigned NOT NULL ,
    price  float not null,
    PRIMARY KEY(routeID),
    FOREIGN KEY(location) REFERENCES stations(id),
    FOREIGN KEY(final_destination) REFERENCES stations(id),
    INDEX(routeID, location, final_destination)
) AUTO_INCREMENT = 1;


create table trips  (
  trip_id mediumint(8) NOT NULL auto_increment,
  train_id mediumint(8) unsigned NOT NULL, 
  routeID  mediumint(8) NOT NULL,
  dt_departure datetime not null,
  duration mediumint as  (timestampdiff(hour, dt_departure, dt_arrival)),
  dt_arrival datetime not null,
  PRIMARY KEY(trip_id),
  FOREIGN KEY(train_id) REFERENCES trains(id),
  FOREIGN KEY(routeID) REFERENCES routes(routeID),
  INDEX(routeID, trip_id)
) AUTO_INCREMENT = 1;


create table payment_methods (
  p_methodID mediumint(8) NOT NULL auto_increment,
  method varchar(255) not null,
  PRIMARY KEY(p_methodID)
) AUTO_INCREMENT = 1;
create table payments (
  paymentID  mediumint(8) NOT NULL auto_increment,
  p_methodID mediumint(8) NOT NULL,
  amount float not null,
  date varchar(255) not null,
  PRIMARY KEY(paymentID ),
  FOREIGN KEY(p_methodID) REFERENCES payment_methods(p_methodID)
) AUTO_INCREMENT = 1;


create table tickets (
  ticket_id  mediumint(8) NOT NULL auto_increment,
  payment_id mediumint(8)  NOT NULL,
  passenger_id   mediumint(8) unsigned not null,
  trip_id   mediumint(8) NOT NULL,
  seat_number  mediumint(8) NOT NULL,
  t_status boolean not null default true,
  PRIMARY KEY(ticket_id),
  FOREIGN KEY(payment_id) REFERENCES payments(paymentID),
  FOREIGN KEY( passenger_id) REFERENCES users(id),
  FOREIGN KEY( trip_id) REFERENCES trips(trip_id),
  FOREIGN KEY(seat_number) REFERENCES seats(seat_number),
  INDEX(ticket_id, trip_id, passenger_id)
) AUTO_INCREMENT = 1;

CREATE TABLE `notification_template` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `sourceId` mediumint(8) unsigned not null, 
  `createdAt` DATETIME NOT NULL,
  `content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`) );
  
  
CREATE TABLE `notifications` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `userId`  MEDIUMINT(8) UNSIGNED NOT NULL,
  `sourceId`  mediumint(8) NOT NULL,
  `sourceType` VARCHAR(50) NOT NULL,
  `type` SMALLINT(6) NOT NULL DEFAULT 0,
  `read` TINYINT(1) NOT NULL DEFAULT 1,
  `trash` TINYINT(1) NOT NULL DEFAULT 1,
  `createdAt` DATETIME NOT NULL,
  `content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_notification_user` (`userId` ASC),
  CONSTRAINT `fk_notification_user`
    FOREIGN KEY (`userId`)
    REFERENCES `users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
