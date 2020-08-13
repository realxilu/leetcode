SELECT Orders.OrderID, Customers.CustomerName
FROM Orders INNER JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;

-- OrderID	CustomerName
-- 10248	Wilman Kala
-- 10249	Tradição Hipermercados
-- 10250	Hanari Carnes
-- 10251	Victuailles en stock
-- 10252	Suprêmes délices
-- 10253	Hanari Carnes
-- 10254	Chop-suey Chinese
-- 10255	Richter Supermarkt
-- 10256	Wellington Importadora
-- 10257	HILARIÓN-Abastos
-- 10258	Ernst Handel
