-- MySQL dump 10.13  Distrib 8.0.37, for Win64 (x86_64)
--
-- Host: localhost    Database: airlines
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `feedbacks`
--

DROP TABLE IF EXISTS `feedbacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedbacks` (
  `email` varchar(30) DEFAULT NULL,
  `message` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedbacks`
--

LOCK TABLES `feedbacks` WRITE;
/*!40000 ALTER TABLE `feedbacks` DISABLE KEYS */;
INSERT INTO `feedbacks` VALUES ('alphabach4@gmail.com','Hi\n');
/*!40000 ALTER TABLE `feedbacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flights` (
  `fid` varchar(10) NOT NULL,
  `departure` varchar(20) DEFAULT NULL,
  `arrival` varchar(20) DEFAULT NULL,
  `ftime` varchar(30) DEFAULT NULL,
  `dtime` varchar(30) DEFAULT NULL,
  `base_price` int DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES ('SHM101','Delhi','Mumbai','2 hours','06:30:00',4500),('SHM102','Bangalore','Hyderabad','3 hours','08:00:00',3500),('SHM103','Chennai','Kolkata','1 hour 30 minutes','09:30:00',4000),('SHM104','Mumbai','Bangalore','2 hours 15 minutes','11:00:00',3900),('SHM105','Delhi','Goa','4 hours','12:30:00',5500),('SHM106','Hyderabad','Ahmedabad','3 hours 45 minutes','14:00:00',4800),('SHM107','Chennai','Mumbai','2 hours 30 minutes','15:30:00',4200),('SHM108','Bangalore','Delhi','5 hours','17:00:00',4700),('SHM109','Goa','Chennai','6 hours','18:30:00',5300),('SHM110','Hyderabad','Bhopal','1 hour 45 minutes','20:00:00',4200),('SHM111','Kolkata','Patna','2 hours 10 minutes','06:00:00',3200),('SHM112','Delhi','Pune','3 hours 20 minutes','08:30:00',3000),('SHM113','Mumbai','Surat','4 hours 5 minutes','10:00:00',2500),('SHM114','Bangalore','Kochi','1 hour 25 minutes','11:30:00',3800),('SHM115','Chennai','Visakhapatnam','2 hours 50 minutes','13:00:00',3700),('SHM116','Hyderabad','Kochi','3 hours 10 minutes','14:30:00',4500),('SHM117','Kolkata','Bhubaneswar','4 hours 30 minutes','16:00:00',3900),('SHM118','Mumbai','Indore','5 hours 15 minutes','17:30:00',5100),('SHM119','Delhi','Chandigarh','6 hours 45 minutes','19:00:00',3500),('SHM120','Goa','Jaipur','1 hour 35 minutes','20:30:00',4200),('SHM121','Delhi','Jaipur','2 hours 5 minutes','06:00:00',3500),('SHM122','Mumbai','Pune','3 hours 25 minutes','08:30:00',3000),('SHM123','Chennai','Madurai','4 hours 15 minutes','10:00:00',2500),('SHM124','Bangalore','Coimbatore','5 hours 50 minutes','12:00:00',4000),('SHM125','Hyderabad','Visakhapatnam','6 hours 30 minutes','14:30:00',5000),('SHM126','Kolkata','Patna','1 hour 20 minutes','16:00:00',3800),('SHM127','Goa','Bengaluru','2 hours 40 minutes','18:30:00',4500),('SHM128','Chennai','Vijayawada','3 hours 55 minutes','20:00:00',4200),('SHM129','Mumbai','Nagpur','4 hours 10 minutes','10:00:00',3700),('SHM130','Delhi','Lucknow','5 hours 5 minutes','12:30:00',3500),('SHM131','Hyderabad','Kochi','6 hours 15 minutes','14:00:00',5500),('SHM132','Kolkata','Ranchi','1 hour 50 minutes','16:30:00',3200),('SHM133','Bangalore','Chandigarh','2 hours 25 minutes','18:00:00',4800),('SHM134','Mumbai','Surat','3 hours 40 minutes','20:00:00',3200),('SHM135','Chennai','Trichy','4 hours 45 minutes','10:30:00',4000),('SHM136','Delhi','Bhopal','5 hours 30 minutes','12:00:00',4400),('SHM137','Goa','Ahmedabad','6 hours 20 minutes','14:30:00',6000),('SHM138','Hyderabad','Indore','1 hour 10 minutes','16:00:00',5300),('SHM139','Kolkata','Chandigarh','2 hours 55 minutes','18:30:00',4600),('SHM140','Mumbai','Patiala','3 hours 35 minutes','20:00:00',3000),('SHM141','Mumbai','Delhi','2 hours 15 minutes','06:30:00',4500),('SHM142','Delhi','Kolkata','2 hours 0 minutes','09:15:00',4200),('SHM143','Chennai','Bangalore','1 hour 0 minutes','07:45:00',2000),('SHM144','Hyderabad','Pune','1 hour 30 minutes','08:30:00',2500),('SHM145','Kolkata','Mumbai','2 hours 45 minutes','10:00:00',5000),('SHM146','Bangalore','Delhi','3 hours 0 minutes','11:15:00',5500),('SHM147','Pune','Chennai','2 hours 30 minutes','12:45:00',4000),('SHM148','Delhi','Hyderabad','2 hours 50 minutes','14:00:00',4800),('SHM149','Mumbai','Bangalore','1 hour 45 minutes','15:30:00',3000),('SHM150','Chennai','Kolkata','2 hours 30 minutes','17:00:00',4700),('SHM151','Kolkata','Hyderabad','3 hours 0 minutes','18:45:00',5300),('SHM152','Delhi','Pune','2 hours 15 minutes','19:30:00',4600),('SHM153','Bangalore','Mumbai','1 hour 50 minutes','21:00:00',3200),('SHM154','Hyderabad','Chennai','1 hour 30 minutes','21:45:00',2800),('SHM155','Pune','Kolkata','3 hours 15 minutes','23:00:00',5400),('SHM156','Delhi','Mumbai','2 hours 10 minutes','05:30:00',4400),('SHM157','Mumbai','Hyderabad','1 hour 25 minutes','07:00:00',2600),('SHM158','Bangalore','Kolkata','2 hours 55 minutes','08:45:00',4900),('SHM159','Chennai','Delhi','2 hours 40 minutes','09:30:00',5200),('SHM160','Hyderabad','Mumbai','1 hour 20 minutes','10:15:00',2500),('SHM161','Kolkata','Bangalore','2 hours 50 minutes','11:45:00',5000),('SHM162','Delhi','Chennai','2 hours 35 minutes','13:00:00',5100),('SHM163','Mumbai','Pune','1 hour 10 minutes','14:30:00',2200),('SHM164','Pune','Hyderabad','1 hour 20 minutes','15:15:00',2400),('SHM165','Bangalore','Mumbai','1 hour 40 minutes','16:45:00',3100),('SHM166','Kolkata','Delhi','2 hours 20 minutes','18:00:00',4700),('SHM167','Delhi','Bangalore','2 hours 55 minutes','19:30:00',5400),('SHM168','Hyderabad','Kolkata','3 hours 5 minutes','21:15:00',5500),('SHM169','Mumbai','Chennai','2 hours 30 minutes','22:45:00',4800),('SHM170','Pune','Delhi','2 hours 25 minutes','23:30:00',4600),('SHM171','Chennai','Hyderabad','1 hour 15 minutes','05:45:00',2300),('SHM172','Delhi','Pune','2 hours 20 minutes','06:15:00',4500),('SHM173','Bangalore','Kolkata','2 hours 45 minutes','07:45:00',4800),('SHM174','Kolkata','Mumbai','2 hours 50 minutes','09:00:00',5200),('SHM175','Hyderabad','Delhi','2 hours 40 minutes','10:30:00',5000),('SHM176','Chennai','Pune','1 hour 50 minutes','05:30:00',2800),('SHM177','Mumbai','Bangalore','1 hour 35 minutes','07:00:00',3000),('SHM178','Delhi','Hyderabad','2 hours 25 minutes','08:15:00',4600),('SHM179','Kolkata','Chennai','2 hours 40 minutes','09:45:00',5100),('SHM180','Hyderabad','Bangalore','1 hour 15 minutes','11:00:00',2700),('SHM181','Bangalore','Pune','1 hour 30 minutes','12:30:00',2900),('SHM182','Pune','Mumbai','1 hour 10 minutes','13:45:00',2200),('SHM183','Mumbai','Delhi','2 hours 20 minutes','15:15:00',4700),('SHM184','Delhi','Kolkata','2 hours 15 minutes','16:45:00',4500),('SHM185','Kolkata','Hyderabad','2 hours 55 minutes','18:00:00',5300),('SHM186','Bangalore','Chennai','1 hour 20 minutes','19:30:00',2400),('SHM187','Chennai','Delhi','2 hours 40 minutes','21:15:00',5100),('SHM188','Hyderabad','Pune','1 hour 10 minutes','22:30:00',2500),('SHM189','Pune','Kolkata','2 hours 50 minutes','23:45:00',5200),('SHM190','Mumbai','Hyderabad','1 hour 25 minutes','06:15:00',2600),('SHM191','Delhi','Chennai','2 hours 35 minutes','07:45:00',5000),('SHM192','Kolkata','Pune','2 hours 45 minutes','09:00:00',5100),('SHM193','Hyderabad','Delhi','2 hours 30 minutes','10:15:00',4900),('SHM194','Chennai','Mumbai','2 hours 25 minutes','11:45:00',4800),('SHM195','Pune','Bangalore','1 hour 30 minutes','13:00:00',2800),('SHM201','Delhi','Dubai','3 hours 40 minutes','06:00:00',18500),('SHM202','Mumbai','Singapore','5 hours 10 minutes','08:15:00',21500),('SHM203','Bangalore','London','10 hours 25 minutes','10:30:00',49500),('SHM204','Hyderabad','Kuala Lumpur','4 hours 30 minutes','12:45:00',19500),('SHM205','Kolkata','Bangkok','2 hours 50 minutes','14:00:00',16500),('SHM206','Chennai','Malé','2 hours 40 minutes','15:15:00',15500),('SHM207','Delhi','Paris','9 hours 15 minutes','16:30:00',52500),('SHM208','Mumbai','New York','16 hours 30 minutes','18:00:00',85500),('SHM209','Bangalore','Dubai','3 hours 45 minutes','19:30:00',18500),('SHM210','Hyderabad','Singapore','4 hours 55 minutes','20:45:00',20500),('SHM211','Kolkata','Tokyo','8 hours 15 minutes','22:00:00',61500),('SHM212','Chennai','Sydney','12 hours 10 minutes','23:15:00',72500),('SHM213','Delhi','Hong Kong','5 hours 25 minutes','01:30:00',23500),('SHM214','Mumbai','Beijing','6 hours 30 minutes','03:45:00',28500),('SHM215','Bangalore','Seoul','8 hours 45 minutes','05:00:00',59500),('SHM216','Hyderabad','London','10 hours 20 minutes','06:15:00',49500),('SHM217','Kolkata','Colombo','3 hours 15 minutes','07:30:00',14500),('SHM218','Chennai','Jakarta','5 hours 5 minutes','08:45:00',21500),('SHM219','Delhi','San Francisco','17 hours 45 minutes','10:00:00',88500),('SHM220','Mumbai','Berlin','8 hours 20 minutes','11:15:00',53500),('SHM221','Bangalore','Frankfurt','9 hours 30 minutes','12:00:00',51500),('SHM222','Hyderabad','Zurich','10 hours 15 minutes','13:30:00',52500),('SHM223','Kolkata','Dubai','3 hours 45 minutes','14:45:00',18500),('SHM224','Chennai','Doha','4 hours 0 minutes','16:00:00',19500),('SHM225','Delhi','Bangkok','4 hours 20 minutes','17:15:00',22500),('SHM226','Mumbai','Tokyo','8 hours 45 minutes','18:30:00',62500),('SHM227','Bangalore','Los Angeles','20 hours 50 minutes','19:45:00',105500),('SHM228','Hyderabad','Toronto','18 hours 35 minutes','21:00:00',95500),('SHM229','Kolkata','Singapore','4 hours 25 minutes','22:15:00',20500),('SHM230','Chennai','Hong Kong','5 hours 30 minutes','23:30:00',23500),('SHM231','Delhi','Melbourne','12 hours 15 minutes','00:45:00',73500),('SHM232','Mumbai','Abu Dhabi','3 hours 10 minutes','02:00:00',17500),('SHM233','Bangalore','Istanbul','7 hours 35 minutes','03:15:00',46500),('SHM234','Hyderabad','Munich','10 hours 50 minutes','04:30:00',53500),('SHM235','Kolkata','Shanghai','5 hours 40 minutes','06:45:00',26500),('SHM236','Chennai','Seoul','8 hours 25 minutes','07:00:00',59500),('SHM237','Delhi','Rome','9 hours 10 minutes','08:30:00',51500),('SHM238','Mumbai','Vienna','8 hours 0 minutes','09:45:00',52500),('SHM239','Bangalore','Sydney','12 hours 35 minutes','11:00:00',73500),('SHM240','Hyderabad','Kuwait City','4 hours 10 minutes','12:15:00',18500),('SHM241','Kolkata','Kuala Lumpur','3 hours 50 minutes','13:30:00',20500),('SHM242','Chennai','Jakarta','5 hours 15 minutes','14:45:00',22500),('SHM243','Delhi','Paris','9 hours 20 minutes','15:00:00',54500),('SHM244','Mumbai','London','9 hours 5 minutes','16:30:00',56500),('SHM245','Bangalore','New York','19 hours 10 minutes','17:45:00',98500),('SHM246','Hyderabad','Manila','6 hours 30 minutes','18:00:00',30500),('SHM247','Kolkata','Bangkok','2 hours 55 minutes','19:15:00',17500),('SHM248','Chennai','Colombo','1 hour 40 minutes','20:30:00',9500),('SHM249','Delhi','Doha','3 hours 50 minutes','21:45:00',22500),('SHM250','Mumbai','Cape Town','11 hours 25 minutes','23:00:00',75500),('SHM251','Dubai','Mumbai','3 hours 15 minutes','05:30:00',21500),('SHM252','Singapore','Chennai','4 hours 10 minutes','07:00:00',19500),('SHM253','London','Delhi','8 hours 45 minutes','09:15:00',62500),('SHM254','New York','Bangalore','18 hours 50 minutes','11:30:00',105500),('SHM255','Bangkok','Kolkata','2 hours 50 minutes','13:00:00',16500),('SHM256','Colombo','Chennai','1 hour 35 minutes','14:30:00',8500),('SHM257','Tokyo','Delhi','9 hours 55 minutes','16:45:00',74500),('SHM258','Jakarta','Hyderabad','5 hours 20 minutes','18:15:00',25500),('SHM259','Kuala Lumpur','Mumbai','5 hours 5 minutes','20:00:00',26500),('SHM260','Doha','Kolkata','4 hours 10 minutes','21:30:00',22500),('SHM261','Paris','Mumbai','9 hours 15 minutes','05:00:00',68500),('SHM262','Dubai','Hyderabad','3 hours 20 minutes','06:30:00',23500),('SHM263','Singapore','Delhi','5 hours 30 minutes','08:15:00',29500),('SHM264','Bangkok','Bangalore','3 hours 15 minutes','09:45:00',18500),('SHM265','Kuala Lumpur','Chennai','4 hours 45 minutes','11:00:00',24500),('SHM266','Jakarta','Kolkata','5 hours 50 minutes','12:30:00',26500),('SHM267','Manila','Mumbai','6 hours 10 minutes','13:45:00',32500),('SHM268','Doha','Chennai','4 hours 5 minutes','15:00:00',21500),('SHM269','Colombo','Trivandrum','1 hour 25 minutes','16:30:00',9500),('SHM270','London','Hyderabad','9 hours 35 minutes','18:15:00',71500),('SHM271','Dubai','Kochi','3 hours 40 minutes','05:15:00',24500),('SHM272','Singapore','Mumbai','5 hours 20 minutes','06:45:00',27500),('SHM273','New York','Delhi','17 hours 50 minutes','08:30:00',99500),('SHM274','Bangkok','Hyderabad','3 hours 10 minutes','09:45:00',17500),('SHM275','Kuala Lumpur','Bangalore','4 hours 50 minutes','10:15:00',23500),('SHM276','Tokyo','Chennai','8 hours 45 minutes','11:30:00',70500),('SHM277','Doha','Mumbai','4 hours 5 minutes','12:45:00',20500),('SHM278','London','Chennai','10 hours 10 minutes','14:00:00',65500),('SHM279','Paris','Delhi','9 hours 30 minutes','15:30:00',71500),('SHM280','Jakarta','Trivandrum','5 hours 35 minutes','16:45:00',25500),('SHM281','Dubai','Ahmedabad','3 hours 15 minutes','17:30:00',22500),('SHM282','Singapore','Hyderabad','5 hours 10 minutes','18:45:00',26500),('SHM283','Bangkok','Mumbai','3 hours 20 minutes','19:30:00',19500),('SHM284','Colombo','Bangalore','1 hour 40 minutes','20:15:00',9500),('SHM285','Doha','Delhi','4 hours 15 minutes','21:00:00',22500),('SHM286','Jakarta','Kochi','5 hours 45 minutes','22:15:00',24500),('SHM287','New York','Mumbai','18 hours 25 minutes','23:45:00',102500),('SHM288','Manila','Kolkata','6 hours 5 minutes','00:30:00',31500),('SHM289','Paris','Chennai','9 hours 25 minutes','01:15:00',69500),('SHM290','London','Bangalore','9 hours 55 minutes','02:45:00',73500),('SHM291','Bangkok','Chennai','3 hours 5 minutes','03:30:00',18500),('SHM292','Tokyo','Kolkata','9 hours 30 minutes','04:15:00',72500),('SHM293','Dubai','Pune','3 hours 25 minutes','05:00:00',23500),('SHM294','Singapore','Delhi','5 hours 45 minutes','06:30:00',29500),('SHM295','Colombo','Kochi','1 hour 25 minutes','07:15:00',8500),('SHM296','Jakarta','Mumbai','6 hours 5 minutes','08:00:00',27500),('SHM297','Doha','Ahmedabad','4 hours 10 minutes','08:45:00',21500),('SHM298','Manila','Delhi','6 hours 15 minutes','09:30:00',32500),('SHM299','London','Mumbai','9 hours 20 minutes','10:15:00',70500),('SHM300','Bangkok','Pune','3 hours 30 minutes','11:00:00',19500),('SHM301','Chennai','Dubai','4 hours 15 minutes','06:30:00',19500),('SHM302','Chennai','Dubai','4 hours 10 minutes','22:45:00',18500),('SHM303','Dubai','Chennai','4 hours 20 minutes','14:30:00',19000),('SHM304','Dubai','Chennai','4 hours 25 minutes','02:15:00',20000);
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger_details`
--

DROP TABLE IF EXISTS `passenger_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger_details` (
  `fid` varchar(10) DEFAULT NULL,
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `inflight_food` varchar(10) DEFAULT NULL,
  `seat_type` varchar(20) DEFAULT NULL,
  `flight_date` date DEFAULT NULL,
  `fare` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger_details`
--

LOCK TABLES `passenger_details` WRITE;
/*!40000 ALTER TABLE `passenger_details` DISABLE KEYS */;
INSERT INTO `passenger_details` VALUES ('SHM105',3064,'Monica.S.M','alphabach4@gmail.com','Female',29,'Veg','Business','2024-12-31',13750),('SHM159',7393,'Ajay','mithilesh.v2007@gmail.com','Male',19,'None','Business','2024-12-24',13000);
/*!40000 ALTER TABLE `passenger_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `email` varchar(40) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('ajaylaxman2404@gmail.com','aaaaa2005','Ajay'),('alphabach4@gmail.com','alpha@123','Alpha'),('mithilesh.v03@gmail.com','Mithu','Mithu'),('mithilesh.v2007@gmail.com','Mithilesh','Mithilesh');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-11  0:27:37
