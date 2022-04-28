CREATE USER 'rohan.backendteam'@'localhost' IDENTIFIED BY 'password1234';
grant usage on *.* to 'rohan.backendteam'@'localhost';

GRANT ALL ON trains TO 'rohan.backendteam'@'localhost';
FLUSH privileges;


CREATE USER 'rony.frontendteam'@'localhost' IDENTIFIED BY '12345678';
grant all on seats to 'rony.frontendteam'@'localhost';

show grants for 'rohan.backendteam'@'localhost';