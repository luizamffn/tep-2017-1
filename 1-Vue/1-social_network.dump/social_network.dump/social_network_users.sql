-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: social_network
-- ------------------------------------------------------
-- Server version	5.7.11-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` text,
  `website` text,
  `name` text,
  `company` json DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` text,
  `address` json DEFAULT NULL,
  `email` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Bret','hildegard.org','Leanne Graham','{\"bs\": \"harness real-time e-markets\", \"name\": \"Romaguera-Crona\", \"catchPhrase\": \"Multi-layered client-server neural-net\"}',1,'1-770-736-8031 x56442','{\"geo\": {\"lat\": \"-37.3159\", \"lng\": \"81.1496\"}, \"city\": \"Gwenborough\", \"suite\": \"Apt. 556\", \"street\": \"Kulas Light\", \"zipcode\": \"92998-3874\"}','Sincere@april.biz'),('Antonette','anastasia.net','Ervin Howell','{\"bs\": \"synergize scalable supply-chains\", \"name\": \"Deckow-Crist\", \"catchPhrase\": \"Proactive didactic contingency\"}',2,'010-692-6593 x09125','{\"geo\": {\"lat\": \"-43.9509\", \"lng\": \"-34.4618\"}, \"city\": \"Wisokyburgh\", \"suite\": \"Suite 879\", \"street\": \"Victor Plains\", \"zipcode\": \"90566-7771\"}','Shanna@melissa.tv'),('Samantha','ramiro.info','Clementine Bauch','{\"bs\": \"e-enable strategic applications\", \"name\": \"Romaguera-Jacobson\", \"catchPhrase\": \"Face to face bifurcated interface\"}',3,'1-463-123-4447','{\"geo\": {\"lat\": \"-68.6102\", \"lng\": \"-47.0653\"}, \"city\": \"McKenziehaven\", \"suite\": \"Suite 847\", \"street\": \"Douglas Extension\", \"zipcode\": \"59590-4157\"}','Nathan@yesenia.net'),('Karianne','kale.biz','Patricia Lebsack','{\"bs\": \"transition cutting-edge web services\", \"name\": \"Robel-Corkery\", \"catchPhrase\": \"Multi-tiered zero tolerance productivity\"}',4,'493-170-9623 x156','{\"geo\": {\"lat\": \"29.4572\", \"lng\": \"-164.2990\"}, \"city\": \"South Elvis\", \"suite\": \"Apt. 692\", \"street\": \"Hoeger Mall\", \"zipcode\": \"53919-4257\"}','Julianne.OConner@kory.org'),('Kamren','demarco.info','Chelsey Dietrich','{\"bs\": \"revolutionize end-to-end systems\", \"name\": \"Keebler LLC\", \"catchPhrase\": \"User-centric fault-tolerant solution\"}',5,'(254)954-1289','{\"geo\": {\"lat\": \"-31.8129\", \"lng\": \"62.5342\"}, \"city\": \"Roscoeview\", \"suite\": \"Suite 351\", \"street\": \"Skiles Walks\", \"zipcode\": \"33263\"}','Lucio_Hettinger@annie.ca'),('Leopoldo_Corkery','ola.org','Mrs. Dennis Schulist','{\"bs\": \"e-enable innovative applications\", \"name\": \"Considine-Lockman\", \"catchPhrase\": \"Synchronised bottom-line interface\"}',6,'1-477-935-8478 x6430','{\"geo\": {\"lat\": \"-71.4197\", \"lng\": \"71.7478\"}, \"city\": \"South Christy\", \"suite\": \"Apt. 950\", \"street\": \"Norberto Crossing\", \"zipcode\": \"23505-1337\"}','Karley_Dach@jasper.info'),('Elwyn.Skiles','elvis.io','Kurtis Weissnat','{\"bs\": \"generate enterprise e-tailers\", \"name\": \"Johns Group\", \"catchPhrase\": \"Configurable multimedia task-force\"}',7,'210.067.6132','{\"geo\": {\"lat\": \"24.8918\", \"lng\": \"21.8984\"}, \"city\": \"Howemouth\", \"suite\": \"Suite 280\", \"street\": \"Rex Trail\", \"zipcode\": \"58804-1099\"}','Telly.Hoeger@billy.biz'),('Maxime_Nienow','jacynthe.com','Nicholas Runolfsdottir V','{\"bs\": \"e-enable extensible e-tailers\", \"name\": \"Abernathy Group\", \"catchPhrase\": \"Implemented secondary concept\"}',8,'586.493.6943 x140','{\"geo\": {\"lat\": \"-14.3990\", \"lng\": \"-120.7677\"}, \"city\": \"Aliyaview\", \"suite\": \"Suite 729\", \"street\": \"Ellsworth Summit\", \"zipcode\": \"45169\"}','Sherwood@rosamond.me'),('Delphine','conrad.com','Glenna Reichert','{\"bs\": \"aggregate real-time technologies\", \"name\": \"Yost and Sons\", \"catchPhrase\": \"Switchable contextually-based project\"}',9,'(775)976-6794 x41206','{\"geo\": {\"lat\": \"24.6463\", \"lng\": \"-168.8889\"}, \"city\": \"Bartholomebury\", \"suite\": \"Suite 449\", \"street\": \"Dayna Park\", \"zipcode\": \"76495-3109\"}','Chaim_McDermott@dana.io'),('Moriah.Stanton','ambrose.net','Clementina DuBuque','{\"bs\": \"target end-to-end models\", \"name\": \"Hoeger LLC\", \"catchPhrase\": \"Centralized empowering task-force\"}',10,'024-648-3804','{\"geo\": {\"lat\": \"-38.2386\", \"lng\": \"57.2232\"}, \"city\": \"Lebsackbury\", \"suite\": \"Suite 198\", \"street\": \"Kattie Turnpike\", \"zipcode\": \"31428-2261\"}','Rey.Padberg@karina.biz');
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

-- Dump completed on 2016-04-05 12:29:03
