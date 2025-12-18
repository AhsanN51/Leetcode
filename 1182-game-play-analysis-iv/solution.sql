select round( sum(if(a1.event_date=a2.plusone and a1.player_id =a2.player_id ,1,0))/count(distinct a1.player_id),2) as fraction
from(select player_id , event_date from Activity  ) as a1
join (select player_id , date_add(min(event_date),interval 1 day) as plusone from Activity group by player_id ) as a2
on a1.player_id =a2.player_id
 
