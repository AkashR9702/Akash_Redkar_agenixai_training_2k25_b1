--Calculate the total number of books currently issued and 
--the percentage of books issued compared to the total available.

--Create Index idx_returndate on transaction(returndate);
Select 
count(*) as Books_issued,
Round((count(*) * 100)/(Select count(*) From bookcopy),2) as Percentage_of_book
From transaction
Where returndate is Null;