-- Task four: Creating a table where a column has a default value.
-- That is, the table is never empty.
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT (1),
       name VARCHAR(256)
);
