# Write your MySQL query statement below
select s.user_id,
round(ifnull(sum(e.action='confirmed')/count(e.user_id),0),2) as confirmation_rate
from Signups as s
left join Confirmations as e
on s.user_id=e.user_id
group by s.user_id