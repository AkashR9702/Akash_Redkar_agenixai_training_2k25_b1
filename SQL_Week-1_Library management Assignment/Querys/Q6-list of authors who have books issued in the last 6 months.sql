--Retrieve a list of authors who have books issued in the last 6 months.

Select Distinct a.authorname 
From author a 
Join book b on a.authorid = b.authorid
Join bookcopy bc on bc.bookid = b.bookid
join transaction t on t.copyid = bc.copyid
Where t.issuedate > current_date - interval '6 months';