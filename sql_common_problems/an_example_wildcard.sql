-- example 1
SELECT *
FROM Customers
WHERE City LIKE 'ber%';

-- CustomerID	CustomerName	ContactName	Address	City	PostalCode	Country
-- 1	Alfreds Futterkiste	Maria Anders	Obere Str. 57	Berlin	12209	Germany
-- 14	Chop-suey Chinese	Yang Wang	Hauptstr. 29	Bern	3012	Switzerland
-- 49	Magazzini Alimentari Riuniti	Giovanni Rovelli	Via Ludovico il Moro 22	Bergamo	24100	Italy

-- example 2
SELECT *
FROM Customers
WHERE City LIKE '%es%';

-- CustomerID	CustomerName	ContactName	Address	City	PostalCode	Country
-- 12	Cactus Comidas para llevar	Patricio Simpson	Cerrito 333	Buenos Aires	1010	Argentina
-- 18	Du monde entier	Janine Labrune	67, rue des Cinquante Otages	Nantes	44000	France
-- 26	France restauration	Carine Schmitt	54, rue Royale	Nantes	44000	France

-- example 3
SELECT *
FROM Customers
WHERE City LIKE 'L_n_on';

-- CustomerID	CustomerName	ContactName	Address	City	PostalCode	Country
-- 4	Around the Horn	Thomas Hardy	120 Hanover Sq.	London	WA1 1DP	UK
-- 11	B's Beverages	Victoria Ashworth	Fauntleroy Circus	London	EC2 5NT	UK