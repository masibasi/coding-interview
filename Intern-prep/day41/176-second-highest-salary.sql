# Write your MySQL query statement below
# https://leetcode.com/problems/second-highest-salary/
# 176-second-highest-salary


select Max(salary) as SecondHighestSalary
From Employee
Where salary < (select Max(salary) from employee)

-- SELECT (
--     SELECT DISTINCT salary
--     FROM (
--         SELECT 
--             salary,
--             DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
--         FROM Employee
--     ) AS RankedSalaries
--     WHERE rnk = 2
-- ) AS SecondHighestSalary;