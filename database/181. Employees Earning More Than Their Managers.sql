-- the idea is to use SELF JOIN for the table and then compare the salaries

SELECT e1.name as Employee
FROM Employee AS e1 JOIN Employee AS e2 
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary
