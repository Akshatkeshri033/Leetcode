-- Last updated: 8/20/2025, 5:48:42 PM
# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id NOT IN (SELECT employee_id FROM Employee WHERE primary_flag = 'Y')
