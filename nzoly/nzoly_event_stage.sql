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
-- Table structure for table `event_stage`
--

DROP TABLE IF EXISTS `event_stage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_stage` (
  `StageID` int NOT NULL AUTO_INCREMENT,
  `StageName` varchar(50) NOT NULL,
  `EventID` int NOT NULL,
  `Location` varchar(50) NOT NULL,
  `StageDate` date NOT NULL,
  `Qualifying` tinyint(1) NOT NULL,
  `PointsToQualify` float DEFAULT NULL,
  PRIMARY KEY (`StageID`),
  KEY `EventID` (`EventID`),
  CONSTRAINT `event_stage_ibfk_1` FOREIGN KEY (`EventID`) REFERENCES `events` (`EventID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=380 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_stage`
--

LOCK TABLES `event_stage` WRITE;
/*!40000 ALTER TABLE `event_stage` DISABLE KEYS */;
INSERT INTO `event_stage` VALUES (281,'Qualification',7,'Genting Snow Park','2022-02-14',1,63.4),(289,'Qualification',11,'Genting Snow Park','2022-02-17',1,70),(290,'Final',11,'Genting Snow Park','2022-02-19',0,NULL),(356,'Heat 1',3,'Shougang','2022-02-14',1,127.5),(357,'Final',3,'Shougang','2022-02-15',0,NULL),(377,'Heat 1',1,'Genting Snow Park','2022-02-05',1,65),(379,'Final',1,'Genting Snow Park','2022-02-06',0,NULL);
/*!40000 ALTER TABLE `event_stage` ENABLE KEYS */;
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
