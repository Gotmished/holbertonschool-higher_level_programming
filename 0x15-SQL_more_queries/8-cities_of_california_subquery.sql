-- Task eight: Listing all cities of California found
-- in the database hbtn_0d_usa. As cities table is linked to states
-- can just draw upon cities table using state_id column
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id ASC;
