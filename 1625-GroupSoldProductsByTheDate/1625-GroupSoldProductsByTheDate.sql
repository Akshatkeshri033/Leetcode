-- Last updated: 8/20/2025, 5:48:51 PM
select 
    sell_date, 
    count(distinct(product)) as num_sold, 
    GROUP_CONCAT(distinct(product) SEPARATOR  ',') as products 
from Activities
group by sell_date 
order by sell_date, product;