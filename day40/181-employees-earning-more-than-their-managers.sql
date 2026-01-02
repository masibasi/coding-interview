# Write your MySQL query statement below
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# 181-employees-earning-more-than-their-managers

SELECT A.name as Employee
From Employee A
left join Employee B
on A.managerId = B.id
WHERE A.salary > B.salary