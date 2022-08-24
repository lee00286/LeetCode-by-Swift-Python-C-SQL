# Write your MySQL query statement below

# ====== JOIN
SELECT w1.id AS Id
FROM Weather w1 JOIN Weather w2 
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
AND w1.temperature > w2.temperature

# # ====== WHERE SUBQUERY
# SELECT w1.id AS Id
# FROM Weather w1 
# WHERE w1.temperature > (
#     SELECT MAX(w2.temperature) AS maxTemp 
#     FROM Weather AS w2
#     WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1);