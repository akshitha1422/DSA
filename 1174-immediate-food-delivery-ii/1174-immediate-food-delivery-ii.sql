# Write your MySQL query statement below
select round(avg(d.order_date=d.customer_pref_delivery_date)*100,2) as immediate_percentage
from Delivery as d
join (select customer_id, min(order_date) as first_order from Delivery group by customer_id) as f
on d.customer_id=f.customer_id
and d.order_date=f.first_order