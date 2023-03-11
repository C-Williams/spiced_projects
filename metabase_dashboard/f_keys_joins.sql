-- CREATE TABLES and insert values
--t1 (auto generated id p_key)               t2

--  name                                  id  value
--  a                                      1   xxx
--  b                                      2   yyy
--  c                                      3   zzz


-- UNIQUE CONSTRAINT

-- show on Insert CONFLICT

-- CHECK CONSTRAINT

-- FOREIGN KEY CONSTRAINT (DELETE RESTRICT/CASCADE)

-- ALTER FOREIGN KEY CONSTRAINT

-- JOINS (INNER/LEFT/RIGHT/CROSS)

--Exercises on northwind DB

-- 1
-- which of our customers never made any orders?
SELECT *
FROM customers as c
LEFT JOIN ORDERS as o
    ON c.customerID = o.customerID
WHERE orderID IS NULL;

-- 2 
--What is the average weight of all the orders, delivered to each country?
-- DO NOT USE THE ORDER COUNTRY , USE THE CUSTOMER COUNTRY 
-- 2nd show the use of having 
SELECT AVG(o.freight) as weight, country
FROM orders as o
JOIN customers as c
   ON o.customerID = c.customerID
GROUP BY country
HAVING AVG(o.freight) > 100
ORDER BY weight DESC;

-- 3
-- What is the total revenue delivered to each country?
   -- e.g. total money made from all orders to each country
-- DO NOT USE THE ORDER COUNTRY, USE THE CUSTOMER COUNTRY
SELECT SUM(unitPrice * quantity * (1-discount)) as revenue, c.country
FROM order_details as od
JOIN orders as o
   ON od.orderID = od.orderID
JOIN customers as c
   ON c.customerID = o.customerID
GROUP BY country
ORDER BY revenue DESC;

-- 4
-- Which employee is making the most money?
SELECT 
    CONCAT(e.firstName, ' ', e.lastName) as name,
    SUM(od.unitPrice * od.quantity * (1-od.discount)) as revenue
FROM employees as e
JOIN orders as o
    ON e.employeeID = o.employeeID
JOIN order_details as od
    ON od.orderID = o.orderID
GROUP BY firstName, lastName
ORDER BY revenue DESC;


-- 5
-- Suppliers/Vendors: who supplies to the company.
SELECT 
    p.supplierID,
    s.companyName,
    p.productName, 
    p.productID, 
    od.orderID, 
    c.companyName
FROM products as p
JOIN order_details as od
    ON p.productID = od.productID
JOIN orders as o
    ON o.orderID = od.orderID
JOIN suppliers as s
    ON s.supplierID = p.supplierID
JOIN customers as c
    ON c.customerID = o.customerID;

-- 6
-- Sales Order transactions: details of the transactions taking place between the customers & the company.
SELECT 
    c.customerID, 
    c.companyName,
    o.orderID,
    od.productID,
    p.productName
FROM customers as c
JOIN orders as o
    ON o.customerID = c.customerID
JOIN order_details as od
    ON od.orderID = o.orderID
JOIN products as p
    ON p.productID = od.productID;

-- 7
-- Which company is the best in terms of revenue?
WITH temp AS (
    SELECT 
        o.orderID,
        ROUND(SUM(unitPrice * quantity * (1-discount)),2) as revenue,
        c.companyName  
    FROM order_details as od
    JOIN orders as o
        ON od.orderID = o.orderID
    JOIN customers as c
        ON c.customerID = o.customerID
    GROUP BY o.orderID, c.companyName
    ORDER BY c.companyName)
SELECT 
    companyName,
    SUM(revenue)
FROM temp
GROUP BY companyName
ORDER BY SUM(revenue) DESC;

-- 8
-- Where do the best customers come from?
WITH temp AS (
    SELECT 
        o.orderID,
        ROUND(SUM(unitPrice * quantity * (1-discount)),2) as revenue,
        c.companyName,
        c.country 
    FROM order_details as od
    JOIN orders as o
        ON od.orderID = o.orderID
    JOIN customers as c
        ON c.customerID = o.customerID
    GROUP BY o.orderID, c.companyName, c.country
    ORDER BY c.companyName)
SELECT 
    SUM(revenue),
    country,
    companyName
FROM temp
GROUP BY country, companyName
ORDER BY sum DESC, country;

-- 9
-- Which products generate the most/least revenue?
SELECT 
    p.productName,
    ROUND(SUM(od.unitPrice * od.quantity * (1-od.discount)),2) as revenue
FROM
    order_details as od
JOIN orders as o
    ON o.orderID = od.orderID
JOIN products as p
    ON p.productID = od.productID
GROUP BY p.productName
ORDER BY revenue DESC;

-- 10
-- Which categories gerate the most/least revenue?
SELECT 
    c.categoryName,
    p.productName,
    ROUND(SUM(od.unitPrice * od.quantity * (1-od.discount)),2) as revenue
FROM
    order_details as od
JOIN orders as o
    ON o.orderID = od.orderID
JOIN products as p
    ON p.productID = od.productID
JOIN categories as c
    ON p.categoryID = c.categoryID
GROUP BY c.categoryName, p.productName
ORDER BY revenue DESC;






SELECT 
    ROUND(avg(od.unitprice * od.quantity)) AS total_revenue
FROM 
    customers AS c
JOIN orders AS o 
    ON o.customerid = c.customerid
JOIN order_details AS od 
    ON od.orderid = o.orderid
WHERE year = '1998' and month = '5'
GROUP BY day, month, year
ORDER BY total_revenue desc;