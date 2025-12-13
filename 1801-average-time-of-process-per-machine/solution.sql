# Write your MySQL query statement below
select machine_id ,
    round(
        sum( CASE
                WHEN activity_type = 'start' THEN -timestamp
                WHEN activity_type = 'end'   THEN  timestamp
            END)
        /count(distinct process_id)
        ,3
    )
    as processing_time
from Activity
group by  machine_id
