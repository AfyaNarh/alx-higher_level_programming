-- script that displays the max temperature of each state (ordered bytate name)
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY state;
