-- Write a SQL query to get the second highest salary FROM the Employee table.
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- NOTE the alias must be "SecondHighestSalary" 
-- v1
SELECT MAX(Salary)
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);

-- v2
select MAX(Salary) AS "SecondHighestSalary" 
FROM Employee 
WHERE Salary != (SELECT MAX(Salary) FROM Employee);

-- v3 use limit
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1, 1) AS SecondHighestSalary
;

-- [KEY] nested sql statement - we can select from another select statement