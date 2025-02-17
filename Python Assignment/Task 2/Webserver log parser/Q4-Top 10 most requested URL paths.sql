Select url, count(*) as URL_Count from apache_logs
Group by url
Order by URL_Count DESC
limit 10;