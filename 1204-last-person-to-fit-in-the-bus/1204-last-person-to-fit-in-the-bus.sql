# Write your MySQL query statement below
select q.person_name
from (select person_name, sum(weight) over (order by turn) as running_wt from Queue) as q
where q.running_wt<=1000
order by q.running_wt desc
limit 1