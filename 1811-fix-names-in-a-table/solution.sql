# Write your MySQL query statement below
select user_id,/*concat(
    upper(substring(name,1,1)),
    lower(substring(name,2)),
    " ",
    upper(substring(name,LOCATE(name," "),1)),
    lower(substring(name,LOCATE(name, " ")))
    ) as name*/
     concat(upper(substr(name, 1,1)), lower(substr(name,2))) as name
from Users
group by user_id
order by user_id
