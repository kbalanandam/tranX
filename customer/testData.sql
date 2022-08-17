CREATE TABLE CustomerType (
  CustomerTypeId INT NOT NULL,
  CustomerType VARCHAR(45) NULL,
  IsAvtive VARCHAR(1) NULL,
  CreatedDate DATETIME NULL,
  CreatedBy VARCHAR(45) NULL,
  UpdatedDate DATETIME NULL,
  UpdatedBy VARCHAR(45) NULL,
  PRIMARY KEY (CustomerTypeId));
  
 Insert Into CustomerType(CustomerTypeId, CustomerType, IsAvtive, CreatedDate, CreatedBy, UpdatedDate, UpdatedBy) VALUES (1, 'Register', 'Y', datetime('now','localtime'), 'MASTERDATA', datetime('now','localtime'), 'MASTERDATA');
 Insert Into CustomerType(CustomerTypeId, CustomerType, IsAvtive, CreatedDate, CreatedBy, UpdatedDate, UpdatedBy) VALUES (2, 'Guest', 'Y', datetime('now','localtime'), 'MASTERDATA', datetime('now','localtime'), 'MASTERDATA');
 
CREATE TABLE Customer (
  CustomerId INTEGER PRIMARY KEY AUTOINCREMENT,
  FirstName VARCHAR(45) NOT NULL,
  MiddleName VARCHAR(45) NULL,
  LastName VARCHAR(45) NOT NULL,
  Gender VARCHAR(1) NOT NULL,
  DateOfBirth DATE NULL,
  CustomerBalance REAL NOT NULL DEFAULT 0.00,
  EffectiveStartDate DATE NULL,
  EffectiveEndDate DATE NULL,
  CustomerTypeId TINYINT NOT NULL,
  AccountStatus TINYINT NULL,
  StatusDateTime DATETIME NULL,
  CreatedDate DATETIME NULL,
  CreatedBy VARCHAR(45) NULL,
  UpdatedDate DATETIME NULL,
  UpdatedBy VARCHAR(45) NULL,
  CONSTRAINT fk_Customer_CustomerType1
    FOREIGN KEY (CustomerTypeId)
    REFERENCES CustomerType (CustomerTypeId));
	
INSERT INTO Customer ( FirstName, LastName, Gender, EffectiveStartDate, CustomerTypeId, AccountStatus, StatusDateTime, CreatedDate, CreatedBy, UpdatedDate ,UpdatedBy)
				VALUES('Bala', 'K', 'G',  datetime('now','localtime'), 1, 1,  datetime('now','localtime'),  datetime('now','localtime'), 'CustomerApi',  datetime('now','localtime'), 'CustomerApi')
