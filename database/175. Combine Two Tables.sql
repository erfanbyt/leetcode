-- using LEFT JOIN in the key idea for this problem.

SELECT firstName, lastName, city, state
FROM Person LEFT JOIN Address ON Person.personID = Address.personId
