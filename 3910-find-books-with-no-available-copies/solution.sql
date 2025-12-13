# Write your MySQL query statement below
select b.book_id , title ,author, genre ,publication_year ,total_copies  as current_borrowers
from library_books l
join borrowing_records b
    on l.book_id=b.book_id
group by b.book_id
having total_copies-(sum(if(return_date is null,1,0))) = 0
order by current_borrowers desc, title asc
