# Write your MySQL query statement below
select round(avg(a2.event_date is not null),2) as fraction
from (select player_id, min(event_date) as first_event from Activity group by player_id) as a1
left join Activity as a2
on a1.player_id=a2.player_id
and a2.event_date=date_add(a1.first_event, interval 1 day)