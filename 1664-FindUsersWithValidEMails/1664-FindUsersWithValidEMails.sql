-- Last updated: 8/20/2025, 5:48:48 PM
# Write your MySQL query statement below
SELECT * FROM users 
WHERE mail IS NOT NULL
AND mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode[.]com$';