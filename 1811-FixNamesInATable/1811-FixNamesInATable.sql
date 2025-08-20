-- Last updated: 8/20/2025, 5:48:47 PM
# Write your MySQL query statement below
SELECT user_id, 
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
