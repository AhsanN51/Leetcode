# Write your MySQL query statement below
select p.product_id  , p.product_name
from Product p
left join Sales s
    on s.product_id=p.product_id 
where sale_date between '2019-01-01' and '2019-03-31' and
p.product_id not in (select s2.product_id from Sales s2 where sale_date not between '2019-01-01' and '2019-03-31')
group by p.product_id
#having count(s.product_id)=1*/
