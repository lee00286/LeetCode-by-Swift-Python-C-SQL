# Write your MySQL query statement below

# Create a table writing specific FROM
SELECT class FROM (SELECT class, 
                   # num = number of occurrences
                   COUNT(DISTINCT student) AS num FROM courses
                   GROUP BY class) AS temp_table
WHERE num >= 5;
