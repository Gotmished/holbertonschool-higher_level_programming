-- Task two: creating a database and a user with SELECT privileges only
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE IF NOT EXISTS USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2)pwd';

GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
