# Write your MySQL query statement below
select person_name
from (select person_name,
sum(weight) over (order by turn) as total_wt
from Queue) as t
where total_wt<=1000
order by total_wt desc
limit 1;