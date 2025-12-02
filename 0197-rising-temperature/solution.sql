# Write your MySQL query statement below
select w2.id
from Weather w1
join Weather w2
on DATE_ADD(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
    where w1.temperature<w2.temperature;
