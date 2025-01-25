--Identify the top 3 customers who have borrowed the most books.

--Create Index idx_customerid on transaction(customerid);
/* Created index for customerid to optimize the Join */
Select c.customername , count(transactionid) as Count_of_Borrow
From customer c
Join transaction t
on c.customerid = t.customerid
Group by c.customerid
Order by Count_of_Borrow DESC
limit 3;
