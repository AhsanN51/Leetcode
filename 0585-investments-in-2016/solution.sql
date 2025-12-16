# Write your MySQL query statement below
select round(sum(i.tiv_2016),2) as tiv_2016
from Insurance i
where i.tiv_2015 in (
    select i1.tiv_2015
    from Insurance i1
    where i.pid !=i1.pid
) and (  
        (i.lat, i.lon ) not in (select i3.lat,i3.lon from Insurance i3 where i.pid!=i3.pid) 
    
)
 
