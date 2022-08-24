# Write your MySQL query statement below
# ======== Where Clause
SELECT name
FROM Customer
WHERE ISNULL(referee_id) OR referee_id != 2;