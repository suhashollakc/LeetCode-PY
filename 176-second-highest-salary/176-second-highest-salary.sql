# Write your MySQL query statement below
SELECT (Select DISTINCT Salary AS SecondHighestSalary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary
