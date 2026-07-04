# Write your MySQL query statement below
select p.product_id, ifnull(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price
from Prices as p
left join UnitsSold as u
on p.product_id=u.product_id
where u.purchase_date between start_date and end_date or purchase_date is null
group by product_id