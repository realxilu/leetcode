SELECT COUNT(CustomerID) Count, Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY Count DESC;

-- Count	Country
-- 13	    USA
-- 11	    France
-- 11	    Germany
-- 9	    Brazil
-- 7	    UK