-- Lists all records from a particular table that contain
-- a value for 'name'
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
