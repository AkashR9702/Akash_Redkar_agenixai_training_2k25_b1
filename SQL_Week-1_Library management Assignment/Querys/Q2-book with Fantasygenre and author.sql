/*List books along with their authors that belong to the "Fantasy" genre,
sorted by publication year in descending order.*/

--Create Index idx_authorid on author(authorid);
--Create Index idx_genre on book(genre);
--EXPLAIN
Select b.title as book_title, 
b.genre as genre ,b.publicationyear, a.authorname 
From book b
join author a 
on b.authorid = a.authorid
Where b.genre = 'Fantasy'
Order by b.publicationyear DESC
