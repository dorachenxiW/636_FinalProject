-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: nzoly
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `event_stage_results`
--

DROP TABLE IF EXISTS `event_stage_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_stage_results` (
  `ResultID` int NOT NULL AUTO_INCREMENT,
  `StageID` int NOT NULL,
  `MemberID` int NOT NULL,
  `PointsScored` float NOT NULL,
  `Position` int DEFAULT NULL,
  PRIMARY KEY (`ResultID`),
  KEY `StageID` (`StageID`),
  KEY `MemberID` (`MemberID`),
  CONSTRAINT `event_stage_results_ibfk_1` FOREIGN KEY (`StageID`) REFERENCES `event_stage` (`StageID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `event_stage_results_ibfk_2` FOREIGN KEY (`MemberID`) REFERENCES `members` (`MemberID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=578 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_stage_results`
--

LOCK TABLES `event_stage_results` WRITE;
/*!40000 ALTER TABLE `event_stage_results` DISABLE KEYS */;
INSERT INTO `event_stage_results` VALUES (222,289,5633,90.5,NULL),(223,290,5633,93,1),(265,281,5632,54.93,NULL),(467,356,5634,176.5,NULL),(538,357,5634,177,2),(567,377,5634,86.75,NULL),(577,379,5634,92.88,1);
/*!40000 ALTER TABLE `event_stage_results` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-11 16:22:06
