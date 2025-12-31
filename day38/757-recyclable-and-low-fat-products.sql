# Write your MySQL query statement below
# https://leetcode.com/problems/recyclable-and-low-fat-products/
# 1757-recyclable-and-low-fat-products

SELECT product_id FROM Products
where low_fats = 'Y'
AND   recyclable = 'Y'