# Write your MySQL query statement below
select product_name, year, price
from Sales
join Product as pr
    on Sales.product_id=pr.product_id
