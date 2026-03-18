# Write your MySQL query statement below
select c.name as customers
from customers as c
where c.id not in(select o.customerid from orders as o);
