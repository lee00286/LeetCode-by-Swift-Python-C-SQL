# Write your MySQL query statement below
SELECT customer_number
FROM (SELECT customer_number, COUNT(customer_number) AS c_count 
      FROM Orders 
      GROUP BY customer_number 
      ORDER BY c_count DESC) AS c
LIMIT 1;