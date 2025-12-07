# Write your MySQL query statement below
select activity_date as day, case
    when activity_type='open_session' then count(distinct user_id)
    when activity_type='end_session' then count(distinct  user_id)
    when activity_type='scroll_down' then count(distinct user_id)
    when activity_type='send_message' then count(distinct user_id)
    end as active_users
from Activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date
