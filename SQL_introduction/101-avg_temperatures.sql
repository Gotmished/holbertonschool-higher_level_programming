-- Imports a database, and returns the average
-- temperature by city
SELECT city, AVG(value) as 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
