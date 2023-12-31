-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flights` (
  `FlightNumber` int NOT NULL AUTO_INCREMENT,
  `DepartureAirport` varchar(50) DEFAULT NULL,
  `DestinationAirport` varchar(50) DEFAULT NULL,
  `DepartureDateTime` datetime DEFAULT NULL,
  `FlightDuration` decimal(4,2) DEFAULT NULL,
  `TotalSeats` int DEFAULT NULL,
  `AvailableSeats` int DEFAULT NULL,
  `FlightClass` varchar(20) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`FlightNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=2219 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES (101,'JFK','LAX','2023-12-03 08:00:00',5.24,150,145,'Economy',600.72),(102,'LAX','FLL','2023-02-17 13:30:00',4.15,150,140,'Economy',500.00),(103,'FLL','ATL','2023-11-10 07:15:00',2.30,100,95,'Business',299.99),(104,'ATL','JFK','2023-11-10 10:00:00',3.23,120,115,'First Class',399.99),(512,'MIA','JFK','2023-10-24 17:41:00',2.54,162,18,'Economy',86.00),(1541,'LGA','ORD','2023-10-23 15:37:00',2.70,162,42,'Economy',107.00),(1781,'FLL','CLT','2023-10-29 11:51:00',2.04,220,103,'Economy',359.00),(2218,'PBI','DFW','2023-10-23 13:22:00',3.12,162,42,'Economy',107.00);
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-08 19:43:33
