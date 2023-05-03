'Get the names and the quantities in stock for each product.'
SELECT productName, unitsInStock, quantityPerUnit
FROM products;

'Get a list of current products (Product ID and name).'
SELECT DISTINCT productID, productName
FROM products;

'Get a list of the most and least expensive products (name and unit price).'
SELECT productName, unitPrice
FROM products
ORDER BY unitPrice DESC
LIMIT 1;

SELECT productName, unitPrice as least_expensive
FROM products
ORDER BY unitPrice ASC
LIMIT 1;

'Get products that cost less than $20.'
SELECT productName, unitPrice
FROM products
WHERE unitPrice < 20;

'Get products that cost between $15 and $25.'
SELECT productName, unitPrice
FROM products
WHERE unitPrice BETWEEN 15 AND 25;

'Get products above average price.'
SELECT productName, unitPrice
FROM products
WHERE unitPrice > (SELECT AVG(unitPrice) from products);

'Find the ten most expensive products.'
SELECT productName, unitPrice
FROM products
ORDER BY unitPrice DESC
LIMIT 10;

'Get a list of discontinued products (Product ID and name).'
SELECT productID, productName
FROM products
WHERE discontinued = 1;

'Count current and discontinued products.'
SELECT COUNT(productID), discontinued
FROM products
GROUP BY discontinued;

'Find products with less units in stock than the quantity on order.'
SELECT productName, unitsInStock, unitsOnOrder
FROM products
WHERE unitsInStock < unitsOnOrder;

'Find the customer who had the highest order amount.'


'Get orders for a given employee and the according customer'
SELECT 
    orders.orderID,
    CONCAT(employees.firstName, ' ', employees.lastName) AS name,
    customers.companyName
FROM employees
JOIN orders
    ON employees.employeeID = orders.employeeID
JOIN customers
    ON customers.customerID = orders.customerID
ORDER BY name;

'Find the hiring age of each employee'
SELECT 
    CONCAT(firstName, ' ', lastName) AS name,
    EXTRACT(year from hireDate)-(EXTRACT(year from birthDate)) AS age_at_hire
FROM employees;

'Create views and/or named queries for some of these queries'
DROP view IF EXISTS "temp";
CREATE view "temp" AS
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
ORDER BY c.companyName;

SELECT 
    SUM(revenue),
    country,
    companyName
FROM temp
GROUP BY country, companyName
ORDER BY sum DESC, country;

SELECT *
FROM orders as o
JOIN country_codes as cc 
    ON o.shipcountry = cc.country;