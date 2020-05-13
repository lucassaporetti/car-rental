CREATE DATABASE IF NOT EXISTS car_rental_db;

USE car_rental_db;

CREATE TABLE CARS (
	UUID char(36) not null unique
    ,NAME varchar(30)
    ,CHASSIS varchar(11) not null unique
    ,COLOR enum('NC','BLACK','RED','GREEN','ORANGE','BLUE','PURPLE','CYAN','GRAY','WHITE','YELLOW','VIOLET')
    ,DOORS tinyint
    ,FUEL enum('GASOLINE','ALCOHOL','FLEX','DIESEL')
    ,PLATE char(8)
    ,PRICE float
    ,AVAILABLE boolean default 1
    ,primary key (UUID)
    ) default charset = utf8;
    
CREATE TABLE EMPLOYEES (
	UUID char(36) not null unique
    ,NAME varchar(30)
    ,AGE tinyint
    ,ADDRESS varchar(120)
    ,PHONE varchar(15)
    ,EMAIL varchar(128)
    ,ACCESS_TYPE enum('ADMIN','MANAGER','ATTENDANT')
    ,HIRED_DATE char(10)
    ,SALARY float
    ,primary key (UUID)
    ) default charset = utf8;
    
CREATE TABLE CUSTOMERS (
	UUID char(36) not null unique
    ,NAME varchar(30)
    ,AGE tinyint
    ,ADDRESS varchar(120)
    ,PHONE varchar(15)
    ,EMAIL varchar(128)
    ,DRV_LICENSE varchar(8)
    ,RENTALS int
    ,primary key (UUID)
    ) default charset = utf8;
	