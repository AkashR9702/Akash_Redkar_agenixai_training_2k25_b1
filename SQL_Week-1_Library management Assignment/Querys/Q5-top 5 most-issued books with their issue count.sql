--Retrieve the top 5 most-issued books with their issue count.
Select b.title as book ,count(transactionid) as IssueCount
From transaction t
Join bookcopy bc 
on t.copyid = bc.copyid
join book b 
on b.bookid = bc.bookid
Group by b.Bookid
Order by IssueCount Desc
limit 5;

