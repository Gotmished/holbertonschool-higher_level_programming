-- Task two: creating a database and a user with SELECT privileges only
-- for all tables within the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2)pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
