--Generate a monthly report of issued books for the past year, 
--showing month, book count, and unique customer count.

Select 
To_char(t.issuedate, 'YYYY-MM') as Month,
count(t.transactionid) as book_count,
count(Distinct t.customerid) as unique_cust_count

From transaction t
Join customer c on t.customerid = c.customerid
Where t.issuedate >= current_date - interval '1 year'
Group by Month
Order by Month;