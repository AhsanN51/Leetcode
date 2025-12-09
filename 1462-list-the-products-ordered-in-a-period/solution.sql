# Write your MySQL query statement below
select product_name , sum(unit) as unit from Products p join Orders o on p.product_id=o.product_id where order_date LIKE '2020-02%' group by product_name having sum(unit)>=100
