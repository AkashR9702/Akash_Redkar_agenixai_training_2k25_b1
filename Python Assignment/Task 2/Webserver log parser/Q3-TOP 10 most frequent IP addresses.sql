Select ip, count(*) as request_count from apache_logs
Group by ip
Order by request_count DESC
limit 10;

