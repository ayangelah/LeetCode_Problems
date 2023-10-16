# Write your MySQL query statement below
SELECT Email from
(SELECT email as Email, COUNT(*) as countemails FROM Person
GROUP BY email) as blah
WHERE countemails > 1