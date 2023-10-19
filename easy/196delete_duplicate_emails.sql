# O(N^2) solution
# Write your MySQL query statement below
DELETE p2 FROM Person p1, Person p2
WHERE p2.email = p1.email AND p2.id > p1.id

# a better but more brute force solution
DELETE FROM Person WHERE 
(email IN 
    (/*duplicate list*/
    SELECT email FROM
    (SELECT email, COUNT(email) as countemail, MIN(id) as smallestid FROM Person GROUP BY email HAVING countemail > 1) as duplicates
    )
AND 
id NOT IN 
    (/*list of lowest id numbers*/
    SELECT smallestid FROM
    (SELECT email, COUNT(email) as countemail, MIN(id) as smallestid FROM Person GROUP BY email HAVING countemail > 1) as duplicates
    )
)