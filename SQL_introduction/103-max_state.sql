-- Displays the maximum temperature of each state
-- using imported database of temperatures
SELECT state, MAX(value) AS 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state;
