-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema customer
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema customer
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `customer` ;
USE `customer` ;

-- -----------------------------------------------------
-- Table `customer`.`CustomerType`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CustomerType` ;

CREATE TABLE IF NOT EXISTS `customer`.`CustomerType` (
  `CustomerTypeId` INT NOT NULL,
  `CustomerType` VARCHAR(45) NULL,
  `IsAvtive` VARCHAR(1) NULL,
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`CustomerTypeId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`Customer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`Customer` ;

CREATE TABLE IF NOT EXISTS `customer`.`Customer` (
  `CustomerId` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(45) NOT NULL,
  `MiddleName` VARCHAR(45) NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `Gender` VARCHAR(1) NOT NULL,
  `DateOfBirth` DATE NULL,
  `CustomerBalance` DECIMAL NULL DEFAULT 0.00,
  `EffectiveStartDate` DATE NULL,
  `EffectiveEndDate` DATE NULL,
  `CustomerTypeId` TINYINT NOT NULL,
  `AccountStatus` TINYINT NULL,
  `StatusDateTime` DATETIME NULL,
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`CustomerId`, `CustomerTypeId`),
  INDEX `fk_Customer_CustomerType1_idx` (`CustomerTypeId` ASC) VISIBLE,
  CONSTRAINT `fk_Customer_CustomerType1`
    FOREIGN KEY (`CustomerTypeId`)
    REFERENCES `customer`.`CustomerType` (`CustomerTypeId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`CusotmerPhones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CusotmerPhones` ;

CREATE TABLE IF NOT EXISTS `customer`.`CusotmerPhones` (
  `PhoneId` INT NOT NULL AUTO_INCREMENT,
  `CustomerId` INT NOT NULL,
  `CountryCode` VARCHAR(5) NULL,
  `PhoneNumber` VARCHAR(20) NULL,
  `IsPrimary` VARCHAR(1) NULL,
  `EffectiveStartDate` DATETIME NULL,
  `EffectiveEndDate` DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`PhoneId`),
  INDEX `fk_userPhones_userAccounts_idx` (`CustomerId` ASC) VISIBLE,
  CONSTRAINT `fk_userPhones_userAccounts`
    FOREIGN KEY (`CustomerId`)
    REFERENCES `customer`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`CustomerEmails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CustomerEmails` ;

CREATE TABLE IF NOT EXISTS `customer`.`CustomerEmails` (
  `EmailId` INT NOT NULL AUTO_INCREMENT,
  `CusotmerId` INT NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `IsPrimary` VARCHAR(1) NOT NULL,
  `StartEffectiveDate` DATETIME NULL,
  `EndEffectiveDate` DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`EmailId`),
  INDEX `fk_userEmails_userAccounts1_idx` (`CusotmerId` ASC) VISIBLE,
  CONSTRAINT `fk_userEmails_userAccounts1`
    FOREIGN KEY (`CusotmerId`)
    REFERENCES `customer`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`CustomerAddress`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CustomerAddress` ;

CREATE TABLE IF NOT EXISTS `customer`.`CustomerAddress` (
  `AddressId` INT NOT NULL AUTO_INCREMENT,
  `CustomerId` INT NOT NULL,
  `Address1` VARCHAR(100) NULL,
  `Address2` VARCHAR(100) NULL,
  `CountryCode` VARCHAR(3) NULL,
  `StateCode` VARCHAR(3) NULL,
  `PostalCode` VARCHAR(10) NULL,
  `StartEffectiveDate` DATETIME NULL,
  `EndEffectiveDate` DATETIME NULL,
  `IsPrimary` VARCHAR(1) NULL,
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`AddressId`),
  INDEX `fk_userAddress_userAccounts1_idx` (`CustomerId` ASC) VISIBLE,
  CONSTRAINT `fk_userAddress_userAccounts1`
    FOREIGN KEY (`CustomerId`)
    REFERENCES `customer`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`CustomerTags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CustomerTags` ;

CREATE TABLE IF NOT EXISTS `customer`.`CustomerTags` (
  `TagId` INT NOT NULL AUTO_INCREMENT,
  `CustomerId` INT NOT NULL,
  `TagSerialNumber` VARCHAR(20) NULL,
  `TagType` TINYINT NULL,
  `TagStatus` VARCHAR(1) NULL,
  `StartEffectiveDate` DATETIME NULL,
  `EndEffectiveDate` DATETIME NULL,
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`TagId`),
  INDEX `fk_userTags_userAccounts1_idx` (`CustomerId` ASC) VISIBLE,
  CONSTRAINT `fk_userTags_userAccounts1`
    FOREIGN KEY (`CustomerId`)
    REFERENCES `customer`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`CusotmerVehicles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CusotmerVehicles` ;

CREATE TABLE IF NOT EXISTS `customer`.`CusotmerVehicles` (
  `VehicleId` INT NOT NULL AUTO_INCREMENT,
  `CustomerId` INT NOT NULL,
  `VehiclePlate` VARCHAR(20) NULL,
  `VehicleClass` TINYINT NULL,
  `VehicleState` VARCHAR(3) NULL,
  `Make` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` SMALLINT(4) NULL,
  `Color` VARCHAR(20) NULL,
  `StartEffectiveDate` DATETIME NULL,
  `EndEffectiveDate` DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`VehicleId`),
  INDEX `fk_userVehicles_userAccounts1_idx` (`CustomerId` ASC) VISIBLE,
  CONSTRAINT `fk_userVehicles_userAccounts1`
    FOREIGN KEY (`CustomerId`)
    REFERENCES `customer`.`Customer` (`CustomerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`CustomerTagVehicles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`CustomerTagVehicles` ;

CREATE TABLE IF NOT EXISTS `customer`.`CustomerTagVehicles` (
  `TagVehicleId` INT NOT NULL AUTO_INCREMENT,
  `TagId` INT NOT NULL,
  `VehicleId` INT NOT NULL,
  `StartEffectiveDate` DATETIME NULL,
  `EndEffectiveDate` DATETIME NULL DEFAULT '9999-12-31 00:00:00',
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`TagVehicleId`),
  INDEX `fk_userTagVehicles_userTags1_idx` (`TagId` ASC) VISIBLE,
  INDEX `fk_userTagVehicles_userVehicles1_idx` (`VehicleId` ASC) VISIBLE,
  CONSTRAINT `fk_userTagVehicles_userTags1`
    FOREIGN KEY (`TagId`)
    REFERENCES `customer`.`CustomerTags` (`TagId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_userTagVehicles_userVehicles1`
    FOREIGN KEY (`VehicleId`)
    REFERENCES `customer`.`CusotmerVehicles` (`VehicleId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`Plazas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`Plazas` ;

CREATE TABLE IF NOT EXISTS `customer`.`Plazas` (
  `PlazaId` INT NOT NULL,
  `PlazaCode` VARCHAR(10) NULL,
  `PlazaDesc` VARCHAR(100) NULL,
  `IsActive` VARCHAR(1) NULL,
  `AgencyId` TINYINT NULL,
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`PlazaId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`Lanes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`Lanes` ;

CREATE TABLE IF NOT EXISTS `customer`.`Lanes` (
  `LaneId` INT NOT NULL,
  `PlazaId` INT NOT NULL,
  `LaneCode` VARCHAR(10) NOT NULL,
  `LaneDesc` VARCHAR(100) NULL,
  `IsActive` VARCHAR(1) NULL,
  `CreatedDate` DATETIME NULL,
  `CreatedBy` VARCHAR(45) NULL,
  `UpdatedDate` DATETIME NULL,
  `UpdatedBy` VARCHAR(45) NULL,
  PRIMARY KEY (`LaneId`, `PlazaId`),
  INDEX `fk_Lanes_Plazas1_idx` (`PlazaId` ASC) VISIBLE,
  CONSTRAINT `fk_Lanes_Plazas1`
    FOREIGN KEY (`PlazaId`)
    REFERENCES `customer`.`Plazas` (`PlazaId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `customer`.`TollRates`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customer`.`TollRates` ;

CREATE TABLE IF NOT EXISTS `customer`.`TollRates` (
  `TollRateId` INT NOT NULL,
  `LaneId` INT NOT NULL,
  `TagRate` DECIMAL NULL,
  `PlateRate` DECIMAL NULL,
  EffectiveStartDate DATETIME NULL,
  EffectiveEndDate DATETIME NULL,
  CreatedDate DATETIME NULL,
  CreatedBy VARCHAR(45) NULL,
  UpdatedDate DATETIME NULL,
  UpdatedBy VARCHAR(45) NULL,
  PRIMARY KEY (TollRateId, LaneId),
  INDEX fk_TollRates_Lanes1_idx (LaneId ASC) VISIBLE,
  CONSTRAINT fk_TollRates_Lanes1
    FOREIGN KEY (LaneId)
    REFERENCES customer.Lanes (LaneId)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
