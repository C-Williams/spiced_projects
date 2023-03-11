-- CATEGORIES --
DROP TABLE IF EXISTS categories CASCADE;

CREATE TABLE categories(
    categoryID SERIAL primary key,
    categoryName VARCHAR,
    description VARCHAR,
    picture BYTEA
);

COPY categories FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/categories.csv' DELIMITER ',' CSV HEADER;

-- COUNTRY CODES --
DROP TABLE IF EXISTS country_codes;

CREATE TABLE country_codes(
    country TEXT,
    code TEXT
);

COPY country_codes FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/country_code.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- REGIONS --
DROP TABLE IF EXISTS regions CASCADE;

CREATE TABLE regions(
    regionID SERIAL primary key,
    regionDescription TEXT
);

COPY regions FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/regions.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- CUSTOMERS --
DROP TABLE IF EXISTS customers CASCADE;

CREATE TABLE customers (
    customerID VARCHAR(20) PRIMARY KEY,
    companyName VARCHAR(150),
    contactName VARCHAR(200),
    contactTitle VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(50),
    region VARCHAR(50),
    postalCode VARCHAR(50),
    country VARCHAR(20),
    phone VARCHAR(25),
    fax VARCHAR(25)
);

COPY customers FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/customers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- EMPLOYEES --
DROP TABLE IF EXISTS employees CASCADE;

CREATE TABLE employees (
    employeeID INT PRIMARY KEY,
    lastName VARCHAR(50),
    firstName VARCHAR(50),
    title VARCHAR(100),
    titleOfCourtesy VARCHAR(15),
    birthDate TIMESTAMP,
    hireDate TIMESTAMP,
    address VARCHAR(150),
    city VARCHAR(20),
    region VARCHAR(20),
    postalCode VARCHAR(20),
    country VARCHAR(20),
    homePhone VARCHAR(25),
    extension VARCHAR(15),
    photo TEXT,
    notes VARCHAR(255),
    reportsTo INT, 
    photoPath VARCHAR(200)
);

COPY employees FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- SHIPPERS --
DROP TABLE IF EXISTS shippers CASCADE;

CREATE TABLE shippers(
    shipperID SERIAL primary key,
    companyName TEXT,
    phone VARCHAR
);

COPY shippers FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/shippers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- SUPPLIERS --
DROP TABLE IF EXISTS suppliers CASCADE;

CREATE TABLE suppliers(
    supplierID SERIAL primary key,
    companyName VARCHAR,
    contactName TEXT,
    contactTitle TEXT,
    address VARCHAR,
    city TEXT,
    region VARCHAR,
    postalCode VARCHAR,
    country TEXT,
    phone VARCHAR,
    fax VARCHAR,
    homePage VARCHAR
);

COPY suppliers FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/suppliers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- TERRITORIES --
DROP TABLE IF EXISTS territories CASCADE;

CREATE TABLE territories(
    territoryID INTEGER primary key,
    territoryDescription TEXT,
    regionID INTEGER,
    FOREIGN KEY (regionID) REFERENCES regions (regionID)
);

COPY territories FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- EMPLOYEE TERRITORIES --
DROP TABLE IF EXISTS employee_territories CASCADE;

CREATE TABLE employee_territories(
    employeeID INTEGER,
    territoryID INTEGER,
    FOREIGN KEY (employeeID) REFERENCES employees (employeeID),
    FOREIGN KEY (territoryID) REFERENCES territories (territoryID)
);

COPY employee_territories FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/employee_territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- ORDERS --
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE orders (
    orderID INT PRIMARY KEY,
    customerID VARCHAR(20),
    employeeID SERIAL,
    orderDate TIMESTAMP,
    requiredDate TIMESTAMP,
    shippedDate TIMESTAMP,
    shipVia INT,
    freight FLOAT,
    shipName VARCHAR(50),
    shipAddress VARCHAR(50),
    shipCity VARCHAR(50),
    shipRegion VARCHAR(50),
    shipPostalCode VARCHAR(20),
    shipCountry VARCHAR(20),
    FOREIGN KEY (customerID) REFERENCES customers (customerID),
    FOREIGN KEY (employeeID) REFERENCES employees (employeeID),
    FOREIGN KEY (shipVia) REFERENCES shippers (shipperID)
);

COPY orders FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/orders.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- PRODUCTS --
DROP TABLE IF EXISTS products CASCADE;

CREATE TABLE products(
    productID SERIAL primary key,
    productName TEXT,
    supplierID INTEGER,
    categoryID INTEGER,
    quantityPerUnit VARCHAR,
    unitPrice NUMERIC,
    unitsInStock INTEGER,
    unitsOnOrder INTEGER,
    reorderLevel INTEGER,
    discontinued INTEGER,
    FOREIGN KEY (supplierID) REFERENCES suppliers (supplierID),
    FOREIGN KEY (categoryID) REFERENCES categories (categoryID)
);

COPY products FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/products.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

-- ORDER DETAILS --
DROP TABLE IF EXISTS order_details;

CREATE TABLE order_details(
    orderID INTEGER,
    productID INTEGER,
    unitPrice NUMERIC,
    quantity INTEGER,
    discount NUMERIC,
    FOREIGN KEY (orderID) REFERENCES orders (orderID),
    FOREIGN KEY (productID) REFERENCES products (productID)
);

COPY order_details FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/order_details.csv' DELIMITER ',' CSV HEADER NULL 'NULL';