# Write your MySQL query statement below
SELECT name as Customers FROM Customers as CT
LEFT JOIN
(SELECT customerId as m_custId, id as m_id FROM Orders) as OT
ON
CT.id = OT.m_custId
WHERE
m_id IS NULL