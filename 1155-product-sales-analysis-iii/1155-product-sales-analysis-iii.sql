# Write your MySQL query statement below
select
    s.product_id,
    s.year as first_year,
    s.quantity,
    s.price
from Sales as s
Join (
    select
    product_id,min(year) as first_year
    from Sales
    group by product_id
) first_sale
on s.product_id=first_sale.product_id
and s.year=first_sale.first_year