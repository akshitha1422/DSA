# Write your MySQL query statement below
select p1.product_id,
ifnull((select p2.new_price 
from Products as p2
where p1.product_id=p2.product_id and change_date<='2019-08-16'
order by change_date desc 
limit 1),10) as price
from (select distinct product_id from Products) as p1