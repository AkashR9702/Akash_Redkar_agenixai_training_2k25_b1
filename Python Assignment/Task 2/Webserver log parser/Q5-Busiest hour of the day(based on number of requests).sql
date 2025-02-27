SELECT EXTRACT(HOUR FROM timestamp) AS hour, COUNT(*) as No_of_Request
FROM apache_logs 
GROUP BY hour 
ORDER BY No_of_Request DESC 
LIMIT 1;
