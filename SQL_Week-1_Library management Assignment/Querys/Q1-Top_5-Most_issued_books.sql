--Retrieve the top 5 most-issued books with their issue count.

--Create Index indx_copyid on transaction(copyid);
--Create Index indx_bookid on bookcopy(bookid);
--Select * from Transaction;
SELECT  b.title as Booktitle ,Count(t.transactionid) as Issuecount 
FROM Transaction t
INNER JOIN BookCopy bc
on t.copyid= bc.copyid

INNER JOIN Book b
on bc.bookid = b.bookid

group by b.title
order by Issuecount desc

limit 5;



