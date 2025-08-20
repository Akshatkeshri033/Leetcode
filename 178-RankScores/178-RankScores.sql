-- Last updated: 8/20/2025, 5:49:22 PM
# Write your MySQL query statement below
# Write your MySQL query statement below
with scores_cte as (
    select id, score,
    dense_rank() over (order by score desc) as "rank"
    from Scores
)

select score, dense_rank() over (order by score desc) as "rank" 
from scores_cte