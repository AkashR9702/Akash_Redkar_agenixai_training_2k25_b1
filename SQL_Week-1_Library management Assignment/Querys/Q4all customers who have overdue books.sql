--List all customers who have overdue books 
--(assume overdue if ReturnDate is null and IssueDate is older than 30 days).

Select  Distinct c.customername
From customer c 
Join transaction t 
on c.customerid = t.customerid
Where t.returndate Is NULL and t.issuedate <  Current_date - Interval '30 days'

