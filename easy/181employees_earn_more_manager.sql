# Write your MySQL query statement below
# selecting an employee table unchanged
SELECT name as Employee
FROM Employee as ET
INNER JOIN
    # selecting manager table
    (SELECT name as m_name, salary as m_salary, id as m_id FROM Employee) as MT
    ON
    # equate
    MT.m_id = ET.managerId
# condition
WHERE salary > m_salary
