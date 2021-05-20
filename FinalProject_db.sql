CREATE TABLE Customers (
    CustomerId INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) DEFAULT NULL,
    LastName VARCHAR(50) DEFAULT NULL,
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(10) DEFAULT NULL
);

CREATE TABLE Stores (
    StoreId INT PRIMARY KEY AUTO_INCREMENT,
    Street VARCHAR(150) DEFAULT NULL,
    City VARCHAR(50) DEFAULT NULL,
    State VARCHAR(50) DEFAULT NULL,
    Zipcode CHAR(5) DEFAULT NULL
);

CREATE TABLE Employees (
    EmployeeId INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) DEFAULT NULL,
    LastName VARCHAR(50) DEFAULT NULL,
    Email VARCHAR(100) DEFAULT NULL,
    Phone VARCHAR(10) DEFAULT NULL,
    StoreId INT DEFAULT NULL,
    KEY StoreId_index (StoreId),
    FOREIGN KEY Employees(StoreId) REFERENCES Stores(StoreId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Brands (
    BrandId INT PRIMARY KEY AUTO_INCREMENT,
    Brand VARCHAR(100) DEFAULT NULL
);

CREATE TABLE Items (
    ItemId INT PRIMARY KEY AUTO_INCREMENT,
    Item VARCHAR(200) DEFAULT NULL,
    Price FLOAT DEFAULT NULL,
    BrandId INT DEFAULT NULL,
    KEY BrandId_index (BrandId),
    FOREIGN KEY Items(BrandId) REFERENCES Brands(BrandId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Sales (
    SaleId INT PRIMARY KEY AUTO_INCREMENT,
    CustomerId INT DEFAULT NULL,
    EmployeeId INT DEFAULT NULL,
    Date DATE DEFAULT NULL,
    KEY CustomerId_index (CustomerId),
    KEY EmployeeId_index (EmployeeId),
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (EmployeeId) REFERENCES Employees(EmployeeId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE SaleItems (
    SaleId INT PRIMARY KEY AUTO_INCREMENT,
    ItemId INT DEFAULT NULL,
    Quantity INT DEFAULT NULL,
    KEY SaleId_index (SaleId),
    KEY ItemId_index (ItemId),
    FOREIGN KEY (SaleId) REFERENCES Sales(SaleId)ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ItemId) REFERENCES Items(ItemId)ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE VIEW vAllStores as
    SELECT Stores.StoreId, Sales.SaleId, SaleItems.ItemId, Price, Quantity
    FROM Stores
    INNER JOIN Employees ON Stores.StoreId = Employees.StoreId
    INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId
    INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId
    INNER JOIN Items ON SaleItems.ItemId = Items.ItemId;

CREATE VIEW vEmployees as
    SELECT Employees.EmployeeId, Employees.StoreId, Sales.SaleId, SaleItems.ItemId, Price, Quantity
    FROM Stores
    INNER JOIN Employees ON Stores.StoreId = Employees.StoreId
    INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId
    INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId
    INNER JOIN Items ON SaleItems.ItemId = Items.ItemId;

CREATE VIEW vCustomers as
    SELECT Customers.CustomerId, Sales.SaleId, SaleItems.ItemId, Price, Quantity
    FROM Stores
    INNER JOIN Employees ON Stores.StoreId = Employees.StoreId
    INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId
    INNER JOIN Customers ON Sales.CustomerId = Customers.CustomerId
    INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId
    INNER JOIN Items ON SaleItems.ItemId = Items.ItemId;

DROP TABLE SaleItems;
DROP TABLE Sales;
DROP TABLE Items;
DROP TABLE Brands;
DROP TABLE Employees;
DROP TABLE Stores;
DROP TABLE Customers;

DROP VIEW vAllStores;
DROP VIEW vEmployees;
DROP VIEW vCustomers;


