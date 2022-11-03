-- Task one: creating a user with all privileges and a password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
-- Not strictly necessary, as an account management statement like GRANT
-- causes grant tables to be reloaded immediately anyway
