-- Task five: creating a table with a default value that is unique
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT (1) UNIQUE,
       name VARCHAR(256)
);
