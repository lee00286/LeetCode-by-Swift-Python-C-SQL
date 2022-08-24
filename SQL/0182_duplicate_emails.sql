# Write your MySQL query statement below
SELECT email AS Email
FROM (SELECT email, COUNT(email) AS duplicate FROM Person GROUP BY email) AS countPerson
WHERE duplicate > 1;