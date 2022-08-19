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
  StartEffectiveDate DATE NULL,
  EndEffectiveDate DATE NULL DEFAULT '9999-12-31 00:00:00',
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
	
INSERT INTO Customer ( customerId, FirstName, LastName, Gender, EffectiveStartDate, CustomerTypeId, AccountStatus, StatusDateTime, CreatedDate, CreatedBy, UpdatedDate ,UpdatedBy)

				VALUES(1, 'Balanandam', 'Koyyalamudi', 'G',  datetime('now','localtime'), 1, 1,  datetime('now','localtime'),  datetime('now','localtime'), 'CustomerApi',  datetime('now','localtime'), 'CustomerApi')
				

CREATE TABLE CustomerEmails (
  EmailId INTEGER PRIMARY KEY AUTOINCREMENT,
  CustomerId INT NOT NULL,
  Email VARCHAR(100) NOT NULL,
  IsPrimary VARCHAR(1) NOT NULL,
  StartEffectiveDate DATETIME NULL,
  EndEffectiveDate DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  CreatedDate DATETIME NULL,
  CreatedBy VARCHAR(45) NULL,
  UpdatedDate DATETIME NULL,
  UpdatedBy VARCHAR(45) NULL,
  CONSTRAINT fk_userEmails_userAccounts1
    FOREIGN KEY (CustomerId)
    REFERENCES Customer (CustomerId));
				
CREATE TABLE CustomerPhones (
  PhoneId INTEGER PRIMARY KEY AUTOINCREMENT,
  CustomerId INT NOT NULL,
  CountryCode VARCHAR(5) NULL,
  PhoneNumber VARCHAR(20) NULL,
  PhoneType VARCHAR(1) NULL,
  StartEffectiveDate DATETIME NULL,
  EndEffectiveDate DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  CreatedDate DATETIME NULL,
  CreatedBy VARCHAR(45) NULL,
  UpdatedDate DATETIME NULL,
  UpdatedBy VARCHAR(45) NULL,
  CONSTRAINT fk_userPhones_userAccounts
    FOREIGN KEY (CustomerId)
    REFERENCES Customer (CustomerId));
	
-- -----------------------------------------------------
-- Table `customer`.`CustomerAddress`
-- -----------------------------------------------------

CREATE TABLE CustomerAddress (
  AddressId INTEGER PRIMARY KEY AUTOINCREMENT,
  CustomerId INT NOT NULL,
  Address1 VARCHAR(100) NULL,
  Address2 VARCHAR(100) NULL,
  CountryCode VARCHAR(3) NULL,
  StateCode VARCHAR(3) NULL,
  PostalCode VARCHAR(10) NULL,
  StartEffectiveDate DATETIME NULL,
  EndEffectiveDate DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  IsPrimary VARCHAR(1) NULL,
  CreatedDate DATETIME NULL,
  CreatedBy VARCHAR(45) NULL,
  UpdatedDate DATETIME NULL,
  UpdatedBy VARCHAR(45) NULL,
  CONSTRAINT fk_userAddress_userAccounts1
    FOREIGN KEY (CustomerId)
    REFERENCES customer.Customer (CustomerId));
