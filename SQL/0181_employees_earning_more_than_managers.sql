# Write your MySQL query statement below
# # ====== JOIN
# SELECT e1.name AS Employee
# FROM Employee AS e1 JOIN Employee AS e2 ON e1.managerId = e2.id AND e1.salary > e2.salary;

# # ====== JOIN subquery
# SELECT name AS Employee
# FROM Employee AS e1 JOIN (
#     SELECT id AS managerId, salary AS managerSalary 
#     FROM Employee) AS e2 ON e1.managerId = e2.managerId
# WHERE salary > managerSalary;

# ====== WHERE
SELECT e1.name AS Employee
FROM Employee AS e1, Employee AS e2 
WHERE e1.managerId = e2.id AND e1.salary > e2.salary;

# # ====== WHERE clause subquery
# SELECT name AS Employee
# FROM Employee AS e1
# WHERE salary > (SELECT salary FROM Employee WHERE e1.managerId = id);