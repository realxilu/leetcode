-- Table: Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.

-- Table: Address
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.

-- Write a SQL query for a report that provides the following information for each person in the Person table, 
-- regardless if there is an address for each of those people:
-- FirstName, LastName, City, State

SELECT Person.FirstName, 
	   Person.LastName, 
	   Address.City, 
	   Address.State
FROM Person LEFT JOIN Address
ON Person.PersonId = Address.PersonId;

-- v2
select p.FirstName, p.LastName, a.City, a.State from Person p left outer join Address a on p.PersonId = a.PersonId

-- [KEY] use left outer join since 'regardless if there is an address for each of those people'