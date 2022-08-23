-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: atcdbinstance.castyrwvsdr7.eu-west-1.rds.amazonaws.com    Database: atc
-- ------------------------------------------------------
-- Server version	8.0.30

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `dexs`
--

DROP TABLE IF EXISTS `dexs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dexs` (
  `dex_id` int NOT NULL AUTO_INCREMENT,
  `network_id` int NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `router_address` varchar(64) DEFAULT NULL,
  `factory_address` varchar(64) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`dex_id`),
  KEY `network_id` (`network_id`),
  CONSTRAINT `dexs_ibfk_1` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=365 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dexs`
--

LOCK TABLES `dexs` WRITE;
/*!40000 ALTER TABLE `dexs` DISABLE KEYS */;
INSERT INTO `dexs` VALUES (1,1,'uniswap_v3_arbitrum',NULL,NULL,'2023-01-05 12:16:59'),(2,1,'kyberswap_elastic_arbitrum',NULL,NULL,'2023-01-05 12:34:10'),(3,1,'sushiswap_arbitrum',NULL,NULL,'2023-01-05 12:34:11'),(4,1,'swapfish',NULL,NULL,'2023-01-05 12:34:11'),(5,1,'oreoswap',NULL,NULL,'2023-01-05 12:34:12'),(6,1,'curve_arbitrum',NULL,NULL,'2023-01-05 12:34:12'),(7,1,'camelot',NULL,NULL,'2023-01-05 12:34:13'),(8,1,'fraxswap_arbitrum',NULL,NULL,'2023-01-05 12:34:13'),(9,1,'3xcalibur',NULL,NULL,'2023-01-05 12:34:14'),(10,1,'swapr_arbitrum',NULL,NULL,'2023-01-05 12:34:14'),(11,1,'elk_finance_arbitrum',NULL,NULL,'2023-01-05 12:34:14'),(12,2,'sushiswap_arbitrum_nova',NULL,NULL,'2023-01-05 12:41:03'),(13,2,'arbswap_arbitrum_nova',NULL,NULL,'2023-01-05 12:41:04'),(14,2,'rcpswap',NULL,NULL,'2023-01-05 12:41:04'),(15,3,'arthswap',NULL,NULL,'2023-01-05 12:41:17'),(16,3,'zenlink_astar',NULL,NULL,'2023-01-05 12:41:17'),(17,3,'starswap',NULL,NULL,'2023-01-05 12:41:18'),(18,3,'versa',NULL,NULL,'2023-01-05 12:41:18'),(19,3,'polkaex_astar',NULL,NULL,'2023-01-05 12:41:19'),(20,3,'ags_finance',NULL,NULL,'2023-01-05 12:41:20'),(21,3,'funbeast',NULL,NULL,'2023-01-05 12:41:20'),(22,3,'astar_exchange',NULL,NULL,'2023-01-05 12:41:20'),(23,4,'trisolaris',NULL,NULL,'2023-01-05 12:41:31'),(24,4,'wannaswap',NULL,NULL,'2023-01-05 12:41:32'),(25,4,'nearpad',NULL,NULL,'2023-01-05 12:41:33'),(26,4,'auroraswap',NULL,NULL,'2023-01-05 12:41:33'),(27,4,'mindgames',NULL,NULL,'2023-01-05 12:41:33'),(28,4,'amaterasu',NULL,NULL,'2023-01-05 12:41:34'),(29,5,'kyberswap_elastic_avalanche',NULL,NULL,'2023-01-05 12:41:45'),(30,5,'traderjoe',NULL,NULL,'2023-01-05 12:41:46'),(31,5,'pangolin',NULL,NULL,'2023-01-05 12:41:46'),(32,5,'radioshack_avalanche',NULL,NULL,'2023-01-05 12:41:47'),(33,5,'sushiswap_avalanche',NULL,NULL,'2023-01-05 12:41:47'),(34,5,'swapsicle',NULL,NULL,'2023-01-05 12:41:48'),(35,5,'fraxswap_avalanche',NULL,NULL,'2023-01-05 12:41:48'),(36,5,'elk_finance_avax',NULL,NULL,'2023-01-05 12:41:49'),(37,5,'kyberswap_classic_avalanche',NULL,NULL,'2023-01-05 12:41:49'),(38,5,'hurricaneswap',NULL,NULL,'2023-01-05 12:41:50'),(39,5,'lydia_finance',NULL,NULL,'2023-01-05 12:41:50'),(40,5,'soulswap_avalanche',NULL,NULL,'2023-01-05 12:41:51'),(41,5,'hakuswap',NULL,NULL,'2023-01-05 12:41:51'),(42,5,'yetiswap',NULL,NULL,'2023-01-05 12:41:51'),(43,5,'thorus',NULL,NULL,'2023-01-05 12:41:52'),(44,5,'firebird_avax',NULL,NULL,'2023-01-05 12:41:53'),(45,5,'baguette',NULL,NULL,'2023-01-05 12:41:53'),(46,5,'spice_trade_avalanche',NULL,NULL,'2023-01-05 12:41:53'),(47,5,'apexswap',NULL,NULL,'2023-01-05 12:41:54'),(48,6,'icecreamswap',NULL,NULL,'2023-01-05 12:42:05'),(49,6,'sphynx_brise',NULL,NULL,'2023-01-05 12:42:05'),(50,7,'diamon_finance',NULL,NULL,'2023-01-05 12:42:43'),(51,8,'kyberswap_classic_bttc',NULL,NULL,'2023-01-05 12:42:54'),(52,8,'torrswap',NULL,NULL,'2023-01-05 12:42:54'),(53,8,'elk_finance_bittorrent',NULL,NULL,'2023-01-05 12:42:55'),(54,9,'pancakeswap_v2',NULL,NULL,'2023-01-05 12:43:06'),(55,9,'biswap',NULL,NULL,'2023-01-05 12:43:07'),(56,9,'fstswap',NULL,NULL,'2023-01-05 12:43:07'),(57,9,'nomiswap_stable',NULL,NULL,'2023-01-05 12:43:08'),(58,9,'apeswap_bsc',NULL,NULL,'2023-01-05 12:43:09'),(59,9,'babyswap',NULL,NULL,'2023-01-05 12:43:09'),(60,9,'nomiswap',NULL,NULL,'2023-01-05 12:43:10'),(61,9,'mdex_bsc',NULL,NULL,'2023-01-05 12:43:10'),(62,9,'leonicornswap',NULL,NULL,'2023-01-05 12:43:11'),(63,9,'babydogeswap',NULL,NULL,'2023-01-05 12:43:12'),(64,9,'mars_ecosystem',NULL,NULL,'2023-01-05 12:43:12'),(65,9,'ellipsis_finance',NULL,NULL,'2023-01-05 12:43:12'),(66,9,'safemoon_swap',NULL,NULL,'2023-01-05 12:43:13'),(67,9,'knightswap',NULL,NULL,'2023-01-05 12:43:13'),(68,9,'bakeryswap',NULL,NULL,'2023-01-05 12:43:14'),(69,9,'dooar_bsc',NULL,NULL,'2023-01-05 12:43:14'),(70,9,'sushiswap_bsc',NULL,NULL,'2023-01-05 12:43:15'),(71,9,'swych',NULL,NULL,'2023-01-05 12:43:16'),(72,9,'cone_exchange',NULL,NULL,'2023-01-05 12:43:16'),(73,9,'winery_swap',NULL,NULL,'2023-01-05 12:43:17'),(74,9,'dinosaureggs',NULL,NULL,'2023-01-05 12:43:17'),(75,9,'planet_finance',NULL,NULL,'2023-01-05 12:43:18'),(76,9,'elk_finance_bsc',NULL,NULL,'2023-01-05 12:43:18'),(77,9,'kyberswap_classic_bsc',NULL,NULL,'2023-01-05 12:43:19'),(78,9,'pandora_digital_swap',NULL,NULL,'2023-01-05 12:43:19'),(79,9,'jetswap_bsc',NULL,NULL,'2023-01-05 12:43:19'),(80,9,'kyberswap_elastic_bsc',NULL,NULL,'2023-01-05 12:43:20'),(81,9,'sphynx_swap',NULL,NULL,'2023-01-05 12:43:21'),(82,9,'yoshi_exchange_bsc',NULL,NULL,'2023-01-05 12:43:21'),(83,9,'wault_finance',NULL,NULL,'2023-01-05 12:43:22'),(84,9,'radioshack_bsc',NULL,NULL,'2023-01-05 12:43:22'),(85,9,'fraxswap_bsc',NULL,NULL,'2023-01-05 12:43:23'),(86,9,'dao_swap',NULL,NULL,'2023-01-05 12:43:23'),(87,9,'baryon_network',NULL,NULL,'2023-01-05 12:43:24'),(88,9,'julswap',NULL,NULL,'2023-01-05 12:43:24'),(89,9,'impossible_finance',NULL,NULL,'2023-01-05 12:43:24'),(90,9,'impossible_finance_v3',NULL,NULL,'2023-01-05 12:43:25'),(91,9,'niob',NULL,NULL,'2023-01-05 12:43:25'),(92,9,'autoshark_finance',NULL,NULL,'2023-01-05 12:43:26'),(93,9,'justmoney_bsc',NULL,NULL,'2023-01-05 12:43:26'),(94,9,'jswap_bsc',NULL,NULL,'2023-01-05 12:43:28'),(95,9,'orbitalswap',NULL,NULL,'2023-01-05 12:43:29'),(96,9,'moonlift',NULL,NULL,'2023-01-05 12:43:29'),(97,9,'pinkswap',NULL,NULL,'2023-01-05 12:43:29'),(98,9,'pls2e',NULL,NULL,'2023-01-05 12:43:30'),(99,9,'alium',NULL,NULL,'2023-01-05 12:43:30'),(100,9,'annex_finance_bsc',NULL,NULL,'2023-01-05 12:43:31'),(101,9,'pyeswap_bsc',NULL,NULL,'2023-01-05 12:43:31'),(102,9,'cakewswap_bsc',NULL,NULL,'2023-01-05 12:43:31'),(103,9,'bridges',NULL,NULL,'2023-01-05 12:43:32'),(104,9,'corgiswap',NULL,NULL,'2023-01-05 12:43:33'),(105,9,'firebird_bsc',NULL,NULL,'2023-01-05 12:43:33'),(106,9,'spice_trade_bsc',NULL,NULL,'2023-01-05 12:43:33'),(107,9,'empiredex_bsc',NULL,NULL,'2023-01-05 12:43:34'),(108,9,'dddx',NULL,NULL,'2023-01-05 12:43:35'),(109,10,'oolongswap',NULL,NULL,'2023-01-05 12:43:47'),(110,10,'swapperchan',NULL,NULL,'2023-01-05 12:43:47'),(111,11,'canto_dex',NULL,NULL,'2023-01-05 12:44:00'),(112,12,'ubeswap',NULL,NULL,'2023-01-05 12:44:12'),(113,12,'sushiswap_celo',NULL,NULL,'2023-01-05 12:44:12'),(114,12,'celodex',NULL,NULL,'2023-01-05 12:44:12'),(115,12,'uniswap_v3_celo',NULL,NULL,'2023-01-05 12:44:13'),(116,13,'huckleberry_clv',NULL,NULL,'2023-01-05 13:22:13'),(117,14,'swappi',NULL,NULL,'2023-01-05 13:22:17'),(118,15,'vvs',NULL,NULL,'2023-01-05 13:22:21'),(119,15,'mm_finance',NULL,NULL,'2023-01-05 13:22:21'),(120,15,'candycity_finance',NULL,NULL,'2023-01-05 13:22:22'),(121,15,'crodex',NULL,NULL,'2023-01-05 13:22:22'),(122,15,'cronaswap',NULL,NULL,'2023-01-05 13:22:23'),(123,15,'cyborgswap',NULL,NULL,'2023-01-05 13:22:23'),(124,15,'elk_finance',NULL,NULL,'2023-01-05 13:22:23'),(125,15,'cougar_exchange',NULL,NULL,'2023-01-05 13:22:24'),(126,15,'crowfi',NULL,NULL,'2023-01-05 13:22:25'),(127,15,'photonswap',NULL,NULL,'2023-01-05 13:22:25'),(128,15,'duckydefi',NULL,NULL,'2023-01-05 13:22:26'),(129,15,'annex_finance',NULL,NULL,'2023-01-05 13:22:26'),(130,15,'aliendex',NULL,NULL,'2023-01-05 13:22:27'),(131,15,'radioshack_cronos',NULL,NULL,'2023-01-05 13:22:27'),(132,15,'empiredex',NULL,NULL,'2023-01-05 13:22:28'),(133,16,'capricorn',NULL,NULL,'2023-01-05 13:22:31'),(134,17,'defi_kingdoms_crystalvale',NULL,NULL,'2023-01-05 13:22:35'),(135,18,'kibbleswap',NULL,NULL,'2023-01-05 13:22:40'),(136,18,'quickswap_dogechain',NULL,NULL,'2023-01-05 13:22:40'),(137,18,'yodeswap',NULL,NULL,'2023-01-05 13:22:41'),(138,18,'dogeswap',NULL,NULL,'2023-01-05 13:22:41'),(139,18,'fraxswap_dogechain',NULL,NULL,'2023-01-05 13:22:42'),(140,18,'dogeshrek',NULL,NULL,'2023-01-05 13:22:42'),(141,18,'radioshack-dogechain',NULL,NULL,'2023-01-05 13:22:43'),(142,18,'bourbon_defi',NULL,NULL,'2023-01-05 13:22:43'),(143,18,'pupswap',NULL,NULL,'2023-01-05 13:22:44'),(144,19,'ech_swap',NULL,NULL,'2023-01-05 13:22:47'),(145,19,'defy_swap',NULL,NULL,'2023-01-05 13:22:48'),(146,20,'glide_finance',NULL,NULL,'2023-01-05 13:22:52'),(147,20,'elk_finance_elastos',NULL,NULL,'2023-01-05 13:22:52'),(148,21,'energiswap',NULL,NULL,'2023-01-05 13:22:58'),(149,22,'uniswap_v3',NULL,NULL,'2023-01-05 13:23:01'),(150,22,'curve',NULL,NULL,'2023-01-05 13:23:02'),(151,22,'uniswap_v2',NULL,NULL,'2023-01-05 13:23:03'),(152,22,'kyberswap_elastic',NULL,NULL,'2023-01-05 13:23:03'),(153,22,'sushiswap',NULL,NULL,'2023-01-05 13:23:04'),(154,22,'shibaswap',NULL,NULL,'2023-01-05 13:23:04'),(155,22,'fraxswap_ethereum',NULL,NULL,'2023-01-05 13:23:04'),(156,22,'pancakeswap_ethereum',NULL,NULL,'2023-01-05 13:23:05'),(157,22,'defi_swap',NULL,NULL,'2023-01-05 13:23:05'),(158,22,'verse',NULL,NULL,'2023-01-05 13:23:06'),(159,22,'swapr_ethereum',NULL,NULL,'2023-01-05 13:23:06'),(160,22,'kyberswap_classic_ethereum',NULL,NULL,'2023-01-05 13:23:07'),(161,22,'templedao',NULL,NULL,'2023-01-05 13:23:07'),(162,22,'dooar_ethereum',NULL,NULL,'2023-01-05 13:23:08'),(163,22,'elk_finance_ethereum',NULL,NULL,'2023-01-05 13:23:09'),(164,22,'unicly',NULL,NULL,'2023-01-05 13:23:09'),(165,22,'concave',NULL,NULL,'2023-01-05 13:23:10'),(166,22,'sakeswap',NULL,NULL,'2023-01-05 13:23:10'),(167,22,'apeswap_ethereum',NULL,NULL,'2023-01-05 13:23:11'),(168,22,'radioshack_ethereum',NULL,NULL,'2023-01-05 13:23:11'),(169,22,'spice_trade_ethereum',NULL,NULL,'2023-01-05 13:23:12'),(170,22,'degenswap',NULL,NULL,'2023-01-05 13:23:12'),(171,22,'standard_ethereum',NULL,NULL,'2023-01-05 13:23:12'),(172,23,'hebeswap',NULL,NULL,'2023-01-05 13:23:26'),(173,24,'uniswap_v2_etf',NULL,NULL,'2023-01-05 13:23:29'),(174,24,'fairswap',NULL,NULL,'2023-01-05 13:23:29'),(175,24,'radioshack-etf',NULL,NULL,'2023-01-05 13:23:31'),(176,25,'uniwswap',NULL,NULL,'2023-01-05 13:23:36'),(177,25,'lfgswap',NULL,NULL,'2023-01-05 13:23:36'),(178,25,'powerswap',NULL,NULL,'2023-01-05 13:23:37'),(179,25,'uniswap_v2_ethpow',NULL,NULL,'2023-01-05 13:23:37'),(180,25,'powswap',NULL,NULL,'2023-01-05 13:23:37'),(181,25,'cakewswap',NULL,NULL,'2023-01-05 13:23:38'),(182,26,'diffusion',NULL,NULL,'2023-01-05 13:23:42'),(183,26,'evmoswap',NULL,NULL,'2023-01-05 13:23:43'),(184,26,'cronus_finance',NULL,NULL,'2023-01-05 13:23:43'),(185,27,'khaos_exchange',NULL,NULL,'2023-01-05 13:23:48'),(186,28,'spookyswap',NULL,NULL,'2023-01-05 13:23:51'),(187,28,'equalizer',NULL,NULL,'2023-01-05 13:23:52'),(188,28,'tomb_swap_fantom',NULL,NULL,'2023-01-05 13:23:52'),(189,28,'wigoswap',NULL,NULL,'2023-01-05 13:23:53'),(190,28,'kyberswap_elastic_fantom',NULL,NULL,'2023-01-05 13:23:53'),(191,28,'spiritswap',NULL,NULL,'2023-01-05 13:23:53'),(192,28,'spiritswap_v2',NULL,NULL,'2023-01-05 13:23:54'),(193,28,'solidly',NULL,NULL,'2023-01-05 13:23:54'),(194,28,'sushiswap_fantom',NULL,NULL,'2023-01-05 13:23:55'),(195,28,'darkknight',NULL,NULL,'2023-01-05 13:23:55'),(196,28,'yoshi_exchange_ftm',NULL,NULL,'2023-01-05 13:23:56'),(197,28,'fraxswap_fantom',NULL,NULL,'2023-01-05 13:23:56'),(198,28,'protofi',NULL,NULL,'2023-01-05 13:23:56'),(199,28,'fbomb_finance',NULL,NULL,'2023-01-05 13:23:57'),(200,28,'soulswap',NULL,NULL,'2023-01-05 13:23:57'),(201,28,'curve_ftm',NULL,NULL,'2023-01-05 13:23:58'),(202,28,'morpheus_swap',NULL,NULL,'2023-01-05 13:23:58'),(203,28,'hyperjump_ftm',NULL,NULL,'2023-01-05 13:23:59'),(204,28,'excalibur',NULL,NULL,'2023-01-05 13:23:59'),(205,28,'paintswap',NULL,NULL,'2023-01-05 13:24:00'),(206,28,'elk_finance_ftm',NULL,NULL,'2023-01-05 13:24:00'),(207,28,'wingswap',NULL,NULL,'2023-01-05 13:24:01'),(208,28,'jetswap_fantom',NULL,NULL,'2023-01-05 13:24:01'),(209,28,'dfyn_fantom',NULL,NULL,'2023-01-05 13:24:02'),(210,28,'radioshack_fantom',NULL,NULL,'2023-01-05 13:24:02'),(211,28,'firebird_fantom',NULL,NULL,'2023-01-05 13:24:02'),(212,29,'fairyswap',NULL,NULL,'2023-01-05 13:24:06'),(213,30,'voltage_finance',NULL,NULL,'2023-01-05 13:24:09'),(214,30,'sushiswap_fuse',NULL,NULL,'2023-01-05 13:24:09'),(215,30,'elk_finance_fuse',NULL,NULL,'2023-01-05 13:24:10'),(216,31,'fx_swap',NULL,NULL,'2023-01-05 13:24:16'),(217,32,'swapr_xdai',NULL,NULL,'2023-01-05 13:24:20'),(218,32,'honeyswap',NULL,NULL,'2023-01-05 13:24:20'),(219,32,'sushiswap_xdai',NULL,NULL,'2023-01-05 13:24:21'),(220,32,'bao_finance',NULL,NULL,'2023-01-05 13:24:21'),(221,32,'levinswap_xdai',NULL,NULL,'2023-01-05 13:24:22'),(222,32,'elk_finance_xdai',NULL,NULL,'2023-01-05 13:24:22'),(223,33,'yokaiswap',NULL,NULL,'2023-01-05 13:24:28'),(224,34,'sushiswap_harmony',NULL,NULL,'2023-01-05 13:24:32'),(225,34,'defi_kingdoms',NULL,NULL,'2023-01-05 13:24:32'),(226,34,'tranquil_finance',NULL,NULL,'2023-01-05 13:24:32'),(227,34,'viperswap',NULL,NULL,'2023-01-05 13:24:33'),(228,34,'openswap',NULL,NULL,'2023-01-05 13:24:33'),(229,34,'fuzz_finance',NULL,NULL,'2023-01-05 13:24:34'),(230,34,'lootswap',NULL,NULL,'2023-01-05 13:24:34'),(231,34,'foxswap',NULL,NULL,'2023-01-05 13:24:35'),(232,34,'hermesdefi',NULL,NULL,'2023-01-05 13:24:35'),(233,34,'elk_finance_one',NULL,NULL,'2023-01-05 13:24:35'),(234,34,'wagmidao',NULL,NULL,'2023-01-05 13:24:36'),(235,34,'bossswap',NULL,NULL,'2023-01-05 13:24:37'),(236,35,'elk_finance_hsc',NULL,NULL,'2023-01-05 13:24:41'),(237,35,'puddingswap',NULL,NULL,'2023-01-05 13:24:41'),(238,36,'mdex',NULL,NULL,'2023-01-05 13:24:46'),(239,36,'makiswap',NULL,NULL,'2023-01-05 13:24:47'),(240,36,'elk_finance_heco',NULL,NULL,'2023-01-05 13:24:47'),(241,37,'mimo',NULL,NULL,'2023-01-05 13:24:52'),(242,37,'elk_finance_iotex',NULL,NULL,'2023-01-05 13:24:53'),(243,38,'kaidex_v3',NULL,NULL,'2023-01-05 13:24:57'),(244,38,'kaidex',NULL,NULL,'2023-01-05 13:24:57'),(245,38,'becoswap',NULL,NULL,'2023-01-05 13:24:58'),(246,39,'surfswap',NULL,NULL,'2023-01-05 13:25:03'),(247,39,'elk_finance_kava',NULL,NULL,'2023-01-05 13:25:03'),(248,39,'jupiter_swap',NULL,NULL,'2023-01-05 13:25:04'),(249,39,'photonswap_kava',NULL,NULL,'2023-01-05 13:25:04'),(250,40,'kekswap',NULL,NULL,'2023-01-05 13:25:07'),(251,41,'klayswap',NULL,NULL,'2023-01-05 13:25:13'),(252,41,'defi_kingdoms_serendale',NULL,NULL,'2023-01-05 13:25:13'),(253,41,'claimswap',NULL,NULL,'2023-01-05 13:25:14'),(254,42,'mojitoswap',NULL,NULL,'2023-01-05 13:25:19'),(255,42,'kuswap',NULL,NULL,'2023-01-05 13:25:20'),(256,42,'elk_finance_kcc',NULL,NULL,'2023-01-05 13:25:20'),(257,43,'voltswap_meter',NULL,NULL,'2023-01-05 13:25:25'),(258,44,'hermes_protocol',NULL,NULL,'2023-01-05 13:25:28'),(259,44,'netswap',NULL,NULL,'2023-01-05 13:25:29'),(260,44,'tethys',NULL,NULL,'2023-01-05 13:25:29'),(261,44,'hyperjump_metis',NULL,NULL,'2023-01-05 13:25:30'),(262,44,'agora_swap',NULL,NULL,'2023-01-05 13:25:30'),(263,44,'standard',NULL,NULL,'2023-01-05 13:25:30'),(264,45,'muesliswap-milkada',NULL,NULL,'2023-01-05 13:26:05'),(265,45,'occamx',NULL,NULL,'2023-01-05 13:26:05'),(266,45,'milkyswap-milkada',NULL,NULL,'2023-01-05 13:26:06'),(267,46,'stellaswap',NULL,NULL,'2023-01-05 13:26:11'),(268,46,'beamswap',NULL,NULL,'2023-01-05 13:26:12'),(269,46,'fraxswap_moonbeam',NULL,NULL,'2023-01-05 13:26:12'),(270,46,'zenlink_moonbeam',NULL,NULL,'2023-01-05 13:26:13'),(271,46,'solarflare',NULL,NULL,'2023-01-05 13:26:13'),(272,46,'lunardex',NULL,NULL,'2023-01-05 13:26:14'),(273,46,'thorus_moonbeam',NULL,NULL,'2023-01-05 13:26:14'),(274,47,'solarbeam',NULL,NULL,'2023-01-05 13:26:17'),(275,47,'zircon',NULL,NULL,'2023-01-05 13:26:18'),(276,47,'zenlink_moonriver',NULL,NULL,'2023-01-05 13:26:18'),(277,47,'huckleberry',NULL,NULL,'2023-01-05 13:26:19'),(278,47,'seadex',NULL,NULL,'2023-01-05 13:26:19'),(279,47,'elk_finance_movr',NULL,NULL,'2023-01-05 13:26:20'),(280,47,'sushiswap_moonriver',NULL,NULL,'2023-01-05 13:26:20'),(281,48,'yuzuswap_oasis_emerald',NULL,NULL,'2023-01-05 13:26:27'),(282,48,'lizard-exchange',NULL,NULL,'2023-01-05 13:26:27'),(283,48,'gemkeeper',NULL,NULL,'2023-01-05 13:26:27'),(284,48,'valleyswap',NULL,NULL,'2023-01-05 13:26:28'),(285,48,'duneswap',NULL,NULL,'2023-01-05 13:26:28'),(286,49,'tealswap',NULL,NULL,'2023-01-05 13:26:32'),(287,50,'okcswap',NULL,NULL,'2023-01-05 13:26:37'),(288,50,'cherryswap',NULL,NULL,'2023-01-05 13:26:37'),(289,50,'kswap',NULL,NULL,'2023-01-05 13:26:38'),(290,50,'jswap',NULL,NULL,'2023-01-05 13:26:38'),(291,50,'elk_finance_oec',NULL,NULL,'2023-01-05 13:26:39'),(292,51,'uniswap_v3_optimism',NULL,NULL,'2023-01-05 13:26:43'),(293,51,'velodrome',NULL,NULL,'2023-01-05 13:26:47'),(294,51,'kyberswap_elastic_optimism',NULL,NULL,'2023-01-05 13:26:48'),(295,51,'curve_optimism',NULL,NULL,'2023-01-05 13:26:50'),(296,51,'kyberswap_classic_optimism',NULL,NULL,'2023-01-05 13:26:50'),(297,51,'fraxswap_optimism',NULL,NULL,'2023-01-05 13:26:50'),(298,51,'zipswap',NULL,NULL,'2023-01-05 13:26:51'),(299,51,'elk_finance_optimism',NULL,NULL,'2023-01-05 13:26:51'),(300,51,'radioshack_optimism',NULL,NULL,'2023-01-05 13:26:52'),(301,52,'dipoleswap',NULL,NULL,'2023-01-05 13:26:57'),(302,53,'quickswap',NULL,NULL,'2023-01-05 13:27:00'),(303,53,'uniswap_v3_polygon_pos',NULL,NULL,'2023-01-05 13:27:01'),(304,53,'quickswap_v3',NULL,NULL,'2023-01-05 13:27:02'),(305,53,'kyberswap_elastic_polygon',NULL,NULL,'2023-01-05 13:27:02'),(306,53,'sushiswap_polygon_pos',NULL,NULL,'2023-01-05 13:27:02'),(307,53,'curve_polygon_pos',NULL,NULL,'2023-01-05 13:27:03'),(308,53,'apeswap_polygon',NULL,NULL,'2023-01-05 13:27:03'),(309,53,'mmfinance_polygon',NULL,NULL,'2023-01-05 13:27:04'),(310,53,'dfyn',NULL,NULL,'2023-01-05 13:27:04'),(311,53,'gravity_finance',NULL,NULL,'2023-01-05 13:27:05'),(312,53,'kyberswap_classic_polygon',NULL,NULL,'2023-01-05 13:27:05'),(313,53,'dystopia',NULL,NULL,'2023-01-05 13:27:06'),(314,53,'fraxswap_polygon_pos',NULL,NULL,'2023-01-05 13:27:06'),(315,53,'vulcandex',NULL,NULL,'2023-01-05 13:27:07'),(316,53,'radioshack_polygon_pos',NULL,NULL,'2023-01-05 13:27:07'),(317,53,'elk_finance_polygon',NULL,NULL,'2023-01-05 13:27:08'),(318,53,'polycat_finance',NULL,NULL,'2023-01-05 13:27:08'),(319,53,'comethswap',NULL,NULL,'2023-01-05 13:27:08'),(320,53,'jetswap_polygon',NULL,NULL,'2023-01-05 13:27:09'),(321,53,'wault_finance_polygon',NULL,NULL,'2023-01-05 13:27:09'),(322,53,'tetuswap',NULL,NULL,'2023-01-05 13:27:10'),(323,53,'polydex',NULL,NULL,'2023-01-05 13:27:11'),(324,53,'auraswap',NULL,NULL,'2023-01-05 13:27:11'),(325,53,'firebird_finance_polygon',NULL,NULL,'2023-01-05 13:27:12'),(326,53,'nachoswap',NULL,NULL,'2023-01-05 13:27:12'),(327,53,'dinoswap',NULL,NULL,'2023-01-05 13:27:13'),(328,53,'honeyswap_polygon',NULL,NULL,'2023-01-05 13:27:14'),(329,53,'justmoney_polygon_pos',NULL,NULL,'2023-01-05 13:27:14'),(330,53,'spice_trade_polygon',NULL,NULL,'2023-01-05 13:27:14'),(331,53,'greenhouse_dex',NULL,NULL,'2023-01-05 13:27:15'),(332,54,'pomswap',NULL,NULL,'2023-01-05 13:27:21'),(333,54,'memeticswap',NULL,NULL,'2023-01-05 13:27:21'),(334,54,'wizardswap',NULL,NULL,'2023-01-05 13:27:22'),(335,55,'dawnswap',NULL,NULL,'2023-01-05 13:27:25'),(336,56,'katana',NULL,NULL,'2023-01-05 13:27:30'),(337,57,'standard_protocol',NULL,NULL,'2023-01-05 13:27:34'),(338,57,'polkaex_shiden',NULL,NULL,'2023-01-05 13:27:34'),(339,58,'tangoswap',NULL,NULL,'2023-01-05 13:27:38'),(340,58,'mistswap',NULL,NULL,'2023-01-05 13:27:38'),(341,58,'benswap',NULL,NULL,'2023-01-05 13:27:39'),(342,58,'emberswap',NULL,NULL,'2023-01-05 13:27:39'),(343,58,'1bch',NULL,NULL,'2023-01-05 13:27:39'),(344,58,'tropical_finance',NULL,NULL,'2023-01-05 13:27:40'),(345,58,'cowswap_smartbch',NULL,NULL,'2023-01-05 13:27:40'),(346,59,'oracleswap',NULL,NULL,'2023-01-05 13:27:46'),(347,59,'pangolin-songbird',NULL,NULL,'2023-01-05 13:27:47'),(348,59,'blazeswap',NULL,NULL,'2023-01-05 13:27:47'),(349,60,'step-exchange',NULL,NULL,'2023-01-05 13:27:51'),(350,61,'sharkswap',NULL,NULL,'2023-01-05 13:27:58'),(351,62,'pegasys',NULL,NULL,'2023-01-05 13:28:03'),(352,63,'apeswap_telos',NULL,NULL,'2023-01-05 13:28:08'),(353,63,'zappy',NULL,NULL,'2023-01-05 13:28:08'),(354,63,'omnidex',NULL,NULL,'2023-01-05 13:28:09'),(355,63,'sushiswap_telos',NULL,NULL,'2023-01-05 13:28:09'),(356,63,'elk_finance_telos',NULL,NULL,'2023-01-05 13:28:10'),(357,64,'laserswap',NULL,NULL,'2023-01-05 13:28:17'),(358,65,'lif3',NULL,NULL,'2023-01-05 13:28:21'),(359,66,'luaswap',NULL,NULL,'2023-01-05 13:28:26'),(360,67,'wagyuswap',NULL,NULL,'2023-01-05 13:28:30'),(361,67,'astroswap',NULL,NULL,'2023-01-05 13:28:31'),(362,68,'wanswap',NULL,NULL,'2023-01-05 13:28:35'),(363,69,'wemix_fi',NULL,NULL,'2023-01-05 13:28:39'),(364,70,'xswap',NULL,NULL,'2023-01-05 13:28:44');
/*!40000 ALTER TABLE `dexs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `networks`
--

DROP TABLE IF EXISTS `networks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `networks` (
  `network_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `chain_number` int DEFAULT NULL,
  `explorer_api_prefix` varchar(255) DEFAULT NULL,
  `explorer_api_key` varchar(255) DEFAULT NULL,
  `explorer_tx_url` varchar(255) DEFAULT NULL,
  `explorer_type` varchar(64) DEFAULT NULL,
  `gas_symbol` varchar(64) DEFAULT NULL,
  `max_gas` decimal(10,0) DEFAULT NULL,
  `min_gas` decimal(10,0) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `chain_rpc_2` varchar(255) DEFAULT NULL,
  `chain_rpc_3` varchar(255) DEFAULT NULL,
  `chain_rpc_4` varchar(255) DEFAULT NULL,
  `chain_rpc_5` varchar(255) DEFAULT NULL,
  `gas_address` varchar(255) DEFAULT NULL,
  `chain_rpc_1` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`network_id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `name_2` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `networks`
--

LOCK TABLES `networks` WRITE;
/*!40000 ALTER TABLE `networks` DISABLE KEYS */;
INSERT INTO `networks` VALUES (1,'arbitrum',42161,'','','EIP3091','https://arbiscan.io','ETH',1,5,'2023-01-04 22:43:06','https://rpc.ankr.com/arbitrum','https://1rpc.io/arb','https://arb-mainnet.g.alchemy.com/v2/demo',NULL,'0x82af49447d8a07e3bd95bd0d56f35241523fbab1','https://arb1.arbitrum.io/rpc'),(2,'arbitrum_nova',42170,'','','EIP3091','https://nova-explorer.arbitrum.io','ETH',1,5,'2023-01-05 12:40:57',NULL,NULL,NULL,NULL,'0x722e8bdd2ce80a4422e880164f2079488e115365','https://nova.arbitrum.io/rpc'),(3,'astr',592,'','','none','https://blockscout.com/astar','ASTR',1,5,'2023-01-05 12:41:10','https://astar.public.blastapi.io','https://evm.astar.network','https://1rpc.io/astr','https://astar-mainnet.g.alchemy.com/v2/demo','0xaeaaf0e2c81af264101b9129c00f4440ccf0f720','https://rpc.astar.network:8545'),(4,'aurora',1313161554,'','','EIP3091','https://aurorascan.dev','NEAR',1,5,'2023-01-05 12:41:26',NULL,NULL,NULL,NULL,'0xc42c30ac6cc15fac9bd938618bcaa1a1fae8501d','https://mainnet.aurora.dev'),(5,'avax',43114,'','','EIP3091','https://avascan.info/blockchain/all','AVAX',1,5,'2023-01-05 12:41:40','https://rpc.ankr.com/avalanche','https://ava-mainnet.public.blastapi.io/ext/bc/C/rpc','https://avalancheapi.terminet.io/ext/bc/C/rpc',NULL,'0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7','https://api.avax.network/ext/bc/C/rpc'),(6,'bitgert',32520,'','','EIP3091','https://brisescan.com','brise',1,5,'2023-01-05 12:41:59','https://nodes.vefinetwork.org/bitgert','https://mainnet-rpc.brisescan.com','https://chainrpc.com','https://serverrpc.com','0x0eb9036cbe0f052386f36170c6b07ef0a0e3f710','https://rpc.icecreamswap.com'),(7,'bitkub_chain',96,'','','none','https://www.bkcscan.com','kub',1,5,'2023-01-05 12:42:11',NULL,NULL,NULL,NULL,'0x67ebd850304c70d983b2d1b93ea79c7cd6c3f6b5','https://rpc.nextsmartchain.com'),(8,'bttc',199,'','','none','https://bttcscan.com','btt',1,5,'2023-01-05 12:42:48',NULL,NULL,NULL,NULL,'0x8d193c6efa90bcff940a98785d1ce9d093d3dc8a','https://rpc.bittorrentchain.io'),(9,'bsc',56,'','','EIP3091','https://bscscan.com','BNB',1,5,'2023-01-05 12:43:00','https://bsc-dataseed1.defibit.io','https://bsc-dataseed1.ninicoin.io','https://bsc-dataseed2.defibit.io',NULL,'0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c','https://bsc-dataseed.binance.org'),(10,'boba',288,'','','none','https://blockexplorer.boba.network','BOBA',1,5,'2023-01-05 12:43:41','https://boba-mainnet.gateway.pokt.network/v1/lb/623ad21b20354900396fed7f','https://lightning-replica.boba.network',NULL,NULL,'0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000','https://mainnet.boba.network'),(11,'canto',7700,'','','none','https://evm.explorer.canto.io','canto',1,5,'2023-01-05 12:43:54',NULL,NULL,NULL,NULL,'0x826551890dc65655a0aceca109ab11abdbd7a07b','https://canto.slingshot.finance'),(12,'celo',42220,'','','EIP3091','https://explorer.celo.org','CELO',1,5,'2023-01-05 12:44:06','https://rpc.ankr.com/celo','https://1rpc.io/celo','wss://forno.celo.org/ws',NULL,'0x471ece3750da237f93b8e339c536989b8978a438','https://forno.celo.org'),(13,'clover_finance',1024,'','','none','https://clvscan.com','clv',1,5,'2023-01-05 13:22:11','https://rpc-ivy-2.clover.finance','https://rpc-ivy-3.clover.finance','https://api-para.clover.finance',NULL,'0x6d6ad95425fcf315c39fa6f3226471d4f16f27b3','https://rpc-ivy.clover.finance'),(14,'cfx',1030,'','','none','https://evm.confluxscan.io','cfx',1,5,'2023-01-05 13:22:15','https://conflux-espace-public.unifra.io',NULL,NULL,NULL,'0x14b2d3bc65e74dae1030eafd8ac30c533c976a9b','https://evm.confluxrpc.com'),(15,'cro',25,'','','none','https://cronos.crypto.org/explorer','CRO',1,5,'2023-01-05 13:22:19','https://cronos-rpc.elk.finance','https://node.croswap.com/rpc',NULL,NULL,'0x5c7f8a570d578ed84e63fdfa7b1ee72deae1ae23','https://evm.cronos.org'),(16,'cube_network',1818,'','','EIP3091','https://cubescan.network','cube',1,5,'2023-01-05 13:22:29','wss://ws-mainnet.cube.network','https://http-mainnet-sg.cube.network','wss://ws-mainnet-sg.cube.network',NULL,'0x9d3f61338d6eb394e378d28c1fd17d5909ac6591','https://http-mainnet.cube.network'),(17,'dfk',53935,'','','none','https://avascan.info/blockchain/dfk','CRYSTAL',1,5,'2023-01-05 13:22:33','https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc',NULL,NULL,NULL,'0x04b9da42306b023f3572e106b11d82aad9d32ebb','https://avax-dfk.gateway.pokt.network/v1/lb/6244818c00b9f0003ad1b619/ext/bc/q2aTwKuyzgs8pynF7UXBZCU7DejbZbZ6EUyHr3JQzYgwNPUPi/rpc'),(18,'dogechain',2000,'','','EIP3091','https://explorer.dogechain.dog','doge',1,5,'2023-01-05 13:22:37','https://rpc-us.dogechain.dog','https://rpc-sg.dogechain.dog','https://rpc.dogechain.dog',NULL,'0xb7ddc6414bf4f5515b52d8bdd69973ae205ff101','https://rpc.dogechain.dog'),(19,'echelon',3000,'','','none','https://app.ech.network/explorer','ech',1,5,'2023-01-05 13:22:46',NULL,NULL,NULL,NULL,'0x4df9da1037108ed96c71fa77b85395cc21a86d60','https://rata.centrality.me/public'),(20,'ela',20,'','','EIP3091','https://esc.elastos.io','ELA',1,5,'2023-01-05 13:22:50','https://api.trinity-tech.io/esc','https://api.elastos.io/eth',NULL,NULL,'0x517e9e5d46c1ea8ab6f78677d6114ef47f71f6c4','https://api.elastos.io/esc'),(21,'nrg',39797,'','','none','https://explorer.energi.network','nrg',1,5,'2023-01-05 13:22:56','https://explorer.energi.network/api/eth-rpc',NULL,NULL,NULL,'0xa55f26319462355474a9f2c8790860776a329aa4','https://nodeapi.energi.network'),(22,'eth',1,'','','EIP3091','https://etherscan.io','ETH',1,5,'2023-01-05 13:22:59','https://rpc.ankr.com/eth','https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7','https://ethereum.publicnode.com',NULL,'0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2','https://eth.llamarpc.com'),(23,'ethereum_classic',61,'','','none','https://www.oklink.com/en/etc','etc',1,5,'2023-01-05 13:23:14','https://etc.etcdesktop.com','https://etc.mytokenpocket.vip','https://besu-de.etc-network.info',NULL,'0x82a618305706b14e7bcf2592d4b9324a366b6dad','https://etc.rivet.link'),(24,'ethereumfair',513100,'','','EIP3091','https://www.oklink.com/en/ethf','ETF',1,5,'2023-01-05 13:23:27',NULL,NULL,NULL,NULL,'0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2','https://rpc.etherfair.org'),(25,'ethw',10001,'','','none','https://www.oklink.com/en/ethw','ethw',1,5,'2023-01-05 13:23:33','https://smartbch.devops.cash/testnet',NULL,NULL,NULL,'0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2','https://rpc-testnet.smartbch.org'),(26,'evmos',9001,'','','none','https://evm.evmos.org','EVMOS',1,5,'2023-01-05 13:23:40','https://evmos-mainnet.gateway.pokt.network/v1/lb/627586ddea1b320039c95205','https://evmos-json-rpc.stakely.io','https://jsonrpc-evmos-ia.cosmosia.notional.ventures',NULL,'0xd4949664cd82660aae99bedc034a0dea8a0bd517','https://eth.bd.evmos.org:8545'),(27,'exosama',2109,'','','EIP3091','https://explorer.exosama.com','SAMA',1,5,'2023-01-05 13:23:45','wss://rpc.exosama.com',NULL,NULL,NULL,'0x8c992cba48189a79204223d106fcb1d797a5f87a','https://rpc.exosama.com'),(28,'ftm',250,'','','EIP3091','https://ftmscan.com','FTM',1,5,'2023-01-05 13:23:49','https://rpc.ftm.tools','https://rpc.ankr.com/fantom','https://rpc.fantom.network',NULL,'0x21be370d5312f44cb42ce377bc9b8a0cef1a4c83','https://fantom-mainnet.gateway.pokt.network/v1/lb/62759259ea1b320039c9e7ac'),(29,'findora',2152,'','','EIP3091','https://evm.findorascan.io','fra',1,5,'2023-01-05 13:24:04',NULL,NULL,NULL,NULL,'0x0000000000000000000000000000000000001000','https://rpc-mainnet.findora.org'),(30,'fuse',122,'','','none','https://explorer.fuse.io','FUSE',1,5,'2023-01-05 13:24:07','https://rpc.fuse.io','https://fuse-mainnet.chainstacklabs.com',NULL,NULL,'0x0be9e53fd7edac9f859882afdda116645287c629','https://fuse-rpc.gateway.pokt.network'),(31,'fx',530,'','','EIP3091','https://starscan.io/evm','FX',1,5,'2023-01-05 13:24:13',NULL,NULL,NULL,NULL,'0x80b5a32e4f032b2a058b4f29ec95eefeeb87adcd','https://fx-json-web3.functionx.io:8545'),(32,'xdai',100,'','','EIP3091','https://blockscout.com/xdai/mainnet','XDAI',1,5,'2023-01-05 13:24:18','https://xdai-rpc.gateway.pokt.network','https://xdai-archive.blockscout.com','https://gnosis-mainnet.public.blastapi.io',NULL,'0xe91d153e0b41518a2ce8dd3d7944fa863463a97d','https://rpc.gnosischain.com'),(33,'godwoken',71402,'','','none','https://v1.gwscan.com','ckb',1,5,'2023-01-05 13:24:25',NULL,NULL,NULL,NULL,'0xc296f806d15e97243a08334256c705ba5c5754cd','https://v1.mainnet.godwoken.io/rpc'),(34,'one',1666600000,'','','EIP3091','https://explorer.harmony.one','ONE',1,5,'2023-01-05 13:24:30','https://api.harmony.one','https://a.api.s0.t.hmny.io','https://api.s0.t.hmny.io',NULL,'0xcf664087a5bb0237a0bad6742852ec6c8d69a27a','https://harmony-0-rpc.gateway.pokt.network'),(35,'hsc',70,'','','EIP3091','https://hooscan.com','hoo',1,5,'2023-01-05 13:24:38','https://http-mainnet2.hoosmartchain.com','wss://ws-mainnet.hoosmartchain.com','wss://ws-mainnet2.hoosmartchain.com',NULL,'0x3eff9d389d13d6352bfb498bcf616ef9b1beac87','https://http-mainnet.hoosmartchain.com'),(36,'heco',128,'','','EIP3091','https://hecoinfo.com','HT',1,5,'2023-01-05 13:24:44','https://http-mainnet.hecochain.com','https://hecoapi.terminet.io/rpc','wss://ws-mainnet.hecochain.com',NULL,'0x5545153ccfca01fbd7dd11c0b23ba694d9509a6f','https://http-mainnet-node.huobichain.com'),(37,'iotx',4689,'','','EIP3091','https://iotexscan.io','IOTX',1,5,'2023-01-05 13:24:50','https://rpc.ankr.com/iotex','https://babel-api.mainnet.iotex.io','https://babel-api.mainnet.iotex.one','https://pokt-api.iotex.io','0xa00744882684c3e4747faefd68d283ea44099d03','https://iotex-mainnet.gateway.pokt.network/v1/lb/6176f902e19001003499f492'),(38,'kai',24,'','','none','https://explorer.kardiachain.io','KAI',1,5,'2023-01-05 13:24:55',NULL,NULL,NULL,NULL,'0xaf984e23eaa3e7967f3c5e007fbe397d8566d23d','https://rpc.kardiachain.io'),(39,'kava',2222,'','','EIP3091','https://explorer.kava.io','kava',1,5,'2023-01-05 13:25:00','https://evm2.kava.io','wss://wevm.kava.io','wss://wevm2.kava.io',NULL,'0xc86c7c0efbd6a49b35e8714c5f59d99de09a225b','https://evm.kava.io'),(40,'kekchain',420420,'','','EIP3091','https://mainnet-explorer.kekchain.com','kek',1,5,'2023-01-05 13:25:06','https://rpc2.kekchain.com','https://kek.interchained.org','https://kekchain.interchained.org',NULL,'0x71ec0cb8f7dd4f4c5bd4204015c4c287fbdaa04a','https://mainnet.kekchain.com'),(41,'klaytn',8217,'','','none','https://scope.klaytn.com','KLAY',1,5,'2023-01-05 13:25:10','https://klaytn01.fandom.finance','https://klaytn02.fandom.finance','https://klaytn03.fandom.finance',NULL,'0xe4f05a66ec68b54a58b17c22107b02e0232cc817','https://public-node-api.klaytnapi.com/v1/cypress'),(42,'kcc',321,'','','EIP3091','https://explorer.kcc.io','KCS',1,5,'2023-01-05 13:25:17','https://kcc.mytokenpocket.vip','https://public-rpc.blockpi.io/http/kcc','https://kcc.getblock.io/mainnet/?api_key=cd77b9bd-ce1c-4a91-89bb-ff2e2c1206c5',NULL,'0x4446fc4eb47f2f6586f9faab68b3498f86c07521','https://rpc-mainnet.kcc.network'),(43,'mtr',82,'','','EIP3091','https://scan.meter.io','MTRG',1,5,'2023-01-05 13:25:23',NULL,NULL,NULL,NULL,'0x228ebbee999c6a7ad74a6130e81b12f9fe237ba3','https://rpc.meter.io'),(44,'metis',1088,'','','EIP3091','https://andromeda-explorer.metis.io','METIS',1,5,'2023-01-05 13:25:26',NULL,NULL,NULL,NULL,'0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000','https://andromeda.metis.io/?owner=1088'),(45,'milkada',2001,'','','none','https://explorer-mainnet-cardano-evm.c1.milkomeda.com','MilkADA',1,5,'2023-01-05 13:26:03','wss://rpc-mainnet-cardano-evm.c1.milkomeda.com',NULL,NULL,NULL,'0xae83571000af4499798d1e3b0fa0070eb3a3e3f9','https://rpc-mainnet-cardano-evm.c1.milkomeda.com'),(46,'glmr',1284,'','','none','https://moonscan.io','GLMR',1,5,'2023-01-05 13:26:09','https://moonbeam.public.blastapi.io','https://rpc.ankr.com/moonbeam','https://1rpc.io/glmr','wss://wss.api.moonbeam.network','0xacc15dc74880c9944775448304b263d191c6077f','https://rpc.api.moonbeam.network'),(47,'movr',1285,'','','none','https://moonriver.moonscan.io','MOVR',1,5,'2023-01-05 13:26:16','https://moonriver.api.onfinality.io/public','https://moonriver.public.blastapi.io','https://rpc.api.moonriver.moonbeam.network','wss://wss.api.moonriver.moonbeam.network','0x98878b06940ae243284ca214f92bb71a2b032b8a','https://moonriver.api.onfinality.io/rpc?apikey=673e1fae-c9c9-4c7f-a3d5-2121e8274366'),(48,'oasis',42262,'','','EIP3091','https://explorer.emerald.oasis.dev','ROSE',1,5,'2023-01-05 13:26:24','wss://emerald.oasis.dev/ws',NULL,NULL,NULL,'0x21c718c22d52d0f3a789b752d4c2fd5908a8a733','https://emerald.oasis.dev'),(49,'oasys',248,'','','EIP3091','https://scan.oasys.games','OAS',1,5,'2023-01-05 13:26:30',NULL,NULL,NULL,NULL,'0x5200000000000000000000000000000000000001','https://rpc.mainnet.oasys.games'),(50,'okexchain',66,'','','EIP3091','https://www.oklink.com/en/oec','OKT',1,5,'2023-01-05 13:26:34','https://okc-mainnet.gateway.pokt.network/v1/lb/6275309bea1b320039c893ff',NULL,NULL,NULL,'0x8f8526dbfd6e38e3d8307702ca8469bae6c56c15','https://exchainrpc.okex.org'),(51,'optimism',10,'','','EIP3091','https://optimistic.etherscan.io','ETH',1,5,'2023-01-05 13:26:41','https://optimism-mainnet.public.blastapi.io','https://rpc.ankr.com/optimism','https://1rpc.io/op','https://opt-mainnet.g.alchemy.com/v2/demo','0x4200000000000000000000000000000000000006','https://mainnet.optimism.io'),(52,'platon_network',210425,'','','none','https://scan.platon.network','LAT',1,5,'2023-01-05 13:26:54','wss://openapi2.platon.network/ws',NULL,NULL,NULL,'0x02406d561069cbed27ef8ea20afd41779a90e2bf','https://openapi2.platon.network/rpc'),(53,'polygon_pos',137,'','','EIP3091','https://polygonscan.com','ETH',1,5,'2023-01-05 13:26:58','https://polygon-rpc.com','https://rpc-mainnet.matic.network','https://rpc-mainnet.maticvigil.com',NULL,'0x7ceb23fd6bc0add59e62ac25578270cff1b9f619','https://polygon.llamarpc.com'),(54,'proof_of_memes',18159,'','','EIP3091','https://explorer.memescan.io','POM',1,5,'2023-01-05 13:27:17','https://mainnet-rpc2.memescan.io','https://mainnet-rpc3.memescan.io','https://mainnet-rpc4.memescan.io',NULL,'0xc84d8d03aa41ef941721a4d77b24bb44d7c7ac55','https://mainnet-rpc.memescan.io'),(55,'redlight_chain',2611,'','','EIP3091','https://redlightscan.finance','REDLC',1,5,'2023-01-05 13:27:23',NULL,NULL,NULL,NULL,'0x00f22f97e249b980a1df5a091fccbd6599600779','https://dataseed2.redlightscan.finance'),(56,'ronin',2020,'','','EIP3091','https://explorer.roninchain.com','eth',1,5,'2023-01-05 13:27:27','https://rpc.publicmint.io:8545',NULL,NULL,NULL,'0xc99a6a985ed2cac1ef41640596c5a5f9f4e19ef5','https://api.roninchain.com/rpc'),(57,'sdn',336,'','','none','https://blockscout.com/shiden','WSDN',1,5,'2023-01-05 13:27:31','https://shiden.public.blastapi.io','https://shiden.api.onfinality.io/public','https://shiden-rpc.dwellir.com',NULL,'0x0f933dc137d21ca519ae4c7e93f87a4c8ef365ef','https://rpc.shiden.astar.network:8545'),(58,'bch',10000,'','','none','https://www.smartscan.cash','BCH',1,5,'2023-01-05 13:27:36','https://global.uat.cash','https://rpc.uatvo.com','https://smartbch.greyh.at',NULL,'0x3743ec0673453e5009310c727ba4eaf7b3a1cc04','https://smartbch.fountainhead.cash/mainnet'),(59,'songbird',19,'','','EIP3091','https://songbird-explorer.flare.network','SGB',1,5,'2023-01-05 13:27:44','https://songbird-api.flare.network/ext/C/rpc','https://songbird.towolabs.com/ext/C/rpc','https://sgb.ftso.com.au/ext/bc/C/rpc',NULL,'0x02f0826ef6ad107cfc861152b32b52fd11bab9ed','https://songbird.towolabs.com/rpc'),(60,'step-network',1234,'','','EIP3091','https://stepscan.io','FITFI',1,5,'2023-01-05 13:27:49',NULL,NULL,NULL,NULL,'0xb58a9d5920af6ac1a9522b0b10f55df16686d1b6','https://rpc.step.network'),(61,'sxn',416,'','','EIP3091','https://explorer.sx.technology','sx',1,5,'2023-01-05 13:27:55',NULL,NULL,NULL,NULL,'0xaa99be3356a11ee92c3f099bd7a038399633566f','https://rpc.sx.technology'),(62,'sys',57,'','','EIP3091','https://explorer.syscoin.org','SYS',1,5,'2023-01-05 13:28:01','https://rpc.ankr.com/syscoin','wss://rpc.syscoin.org/wss',NULL,NULL,'0xd3e822f3ef011ca5f17d82c956d952d8d7c3a1bb','https://rpc.syscoin.org'),(63,'tlos',40,'','','EIP3091','https://www.teloscan.io','WTLOS',1,5,'2023-01-05 13:28:06','https://rpc1.eu.telos.net/evm','https://rpc1.us.telos.net/evm','https://rpc2.us.telos.net/evm',NULL,'0xd102ce6a4db07d247fcc28f366a623df0938ca9e','https://mainnet.telos.net/evm'),(64,'thundercore',108,'','','EIP3091','https://viewblock.io/thundercore','tt',1,5,'2023-01-05 13:28:15','https://mainnet-rpc.thundertoken.net','https://mainnet-rpc.thundercore.io',NULL,NULL,'0x413cefea29f2d07b8f2acfa69d92466b9535f717','https://mainnet-rpc.thundercore.com'),(65,'tombchain',6969,'','','none','https://tombscout.com','tomb',1,5,'2023-01-05 13:28:18',NULL,NULL,NULL,NULL,'0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000','https://rpc.tombchain.com'),(66,'tomochain',88,'','','none','https://tomoscan.io','tomo',1,5,'2023-01-05 13:28:23',NULL,NULL,NULL,NULL,'0xb1f66997a5760428d3a87d68b90bfe0ae64121cc','https://rpc.tomochain.com'),(67,'velas',106,'','','EIP3091','https://evmexplorer.velas.com','VLX',1,5,'2023-01-05 13:28:27','https://velas-mainnet.rpcfast.com?api_key=S3X5aFCCW9MobqVatVZX93fMtWCzff0MfRj9pvjGKSiX5Nas7hz33HwwlrT5tXRM','https://explorer.velas.com/rpc',NULL,NULL,'0xc579d1f3cf86749e05cd06f7ade17856c2ce3126','https://evmexplorer.velas.com/rpc'),(68,'wan',888,'','','none','https://www.wanscan.org','wan',1,5,'2023-01-05 13:28:33',NULL,NULL,NULL,NULL,'0xdabd997ae5e4799be47d6e69d9431615cba28f48','https://gwan-ssl.wandevs.org:56891'),(69,'wemix',1111,'','','EIP3091','https://explorer.wemix.com','WEMIX',1,5,'2023-01-05 13:28:37','wss://ws.wemix.com',NULL,NULL,NULL,'0x7d72b22a74a216af4a002a1095c8c707d6ec1c5f','https://api.wemix.com'),(70,'xdc',50,'','','EIP3091','https://explorer.xinfin.network','xdc',1,5,'2023-01-05 13:28:42','https://rpc.xinfin.network','https://rpc1.xinfin.network',NULL,NULL,'0x951857744785e80e2de051c32ee7b25f9c458c42','https://erpc.xinfin.network');
/*!40000 ALTER TABLE `networks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pair_market_data`
--

DROP TABLE IF EXISTS `pair_market_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pair_market_data` (
  `pair_marketdata_id` int NOT NULL AUTO_INCREMENT,
  `pair_id` int NOT NULL,
  `network_id` int NOT NULL,
  `dex_id` int NOT NULL,
  `ranking` int NOT NULL,
  `liquidity` bigint NOT NULL,
  `volume` bigint NOT NULL,
  `fdv` bigint NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pair_marketdata_id`),
  KEY `pair_id` (`pair_id`),
  KEY `network_id` (`network_id`),
  KEY `dex_id` (`dex_id`),
  CONSTRAINT `pair_market_data_ibfk_1` FOREIGN KEY (`pair_id`) REFERENCES `pairs` (`pair_id`) ON DELETE CASCADE,
  CONSTRAINT `pair_market_data_ibfk_2` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`) ON DELETE CASCADE,
  CONSTRAINT `pair_market_data_ibfk_3` FOREIGN KEY (`dex_id`) REFERENCES `dexs` (`dex_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pair_market_data`
--

LOCK TABLES `pair_market_data` WRITE;
/*!40000 ALTER TABLE `pair_market_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `pair_market_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pairs`
--

DROP TABLE IF EXISTS `pairs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pairs` (
  `pair_id` int NOT NULL AUTO_INCREMENT,
  `primary_token_id` int NOT NULL,
  `secondary_token_id` int NOT NULL,
  `network_id` int NOT NULL,
  `dex_id` int NOT NULL,
  `name` varchar(64) NOT NULL,
  `address` varchar(640) NOT NULL,
  `analysed` tinyint(1) DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pair_id`),
  UNIQUE KEY `unique_network_pair` (`network_id`,`address`),
  KEY `dex_id` (`dex_id`),
  KEY `primary_token_id` (`primary_token_id`),
  KEY `secondary_token_id` (`secondary_token_id`),
  CONSTRAINT `pairs_ibfk_1` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`) ON DELETE CASCADE,
  CONSTRAINT `pairs_ibfk_2` FOREIGN KEY (`dex_id`) REFERENCES `dexs` (`dex_id`) ON DELETE CASCADE,
  CONSTRAINT `pairs_ibfk_3` FOREIGN KEY (`primary_token_id`) REFERENCES `tokens` (`token_id`) ON DELETE CASCADE,
  CONSTRAINT `pairs_ibfk_4` FOREIGN KEY (`secondary_token_id`) REFERENCES `tokens` (`token_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pairs`
--

LOCK TABLES `pairs` WRITE;
/*!40000 ALTER TABLE `pairs` DISABLE KEYS */;
/*!40000 ALTER TABLE `pairs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routes`
--

DROP TABLE IF EXISTS `routes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routes` (
  `route_id` int NOT NULL AUTO_INCREMENT,
  `network_id` int NOT NULL,
  `dex_id` int NOT NULL,
  `pair_id` int DEFAULT NULL,
  `token_in_id` int DEFAULT NULL,
  `token_out_id` int DEFAULT NULL,
  `token_in_address` varchar(64) DEFAULT NULL,
  `token_out_address` varchar(64) DEFAULT NULL,
  `route` varchar(640) NOT NULL,
  `method` varchar(64) DEFAULT NULL,
  `transaction_hash` varchar(255) NOT NULL,
  `block_number` int NOT NULL,
  `amount_in` decimal(38,0) DEFAULT NULL,
  `amount_out` decimal(38,0) DEFAULT NULL,
  `tx_timestamp` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`route_id`),
  KEY `network_id` (`network_id`),
  KEY `dex_id` (`dex_id`),
  KEY `pair_id` (`pair_id`),
  KEY `token_in_id` (`token_in_id`),
  KEY `token_out_id` (`token_out_id`),
  CONSTRAINT `routes_ibfk_1` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`) ON DELETE CASCADE,
  CONSTRAINT `routes_ibfk_2` FOREIGN KEY (`dex_id`) REFERENCES `dexs` (`dex_id`) ON DELETE CASCADE,
  CONSTRAINT `routes_ibfk_3` FOREIGN KEY (`pair_id`) REFERENCES `pairs` (`pair_id`) ON DELETE CASCADE,
  CONSTRAINT `routes_ibfk_4` FOREIGN KEY (`token_in_id`) REFERENCES `tokens` (`token_id`) ON DELETE CASCADE,
  CONSTRAINT `routes_ibfk_5` FOREIGN KEY (`token_out_id`) REFERENCES `tokens` (`token_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routes`
--

LOCK TABLES `routes` WRITE;
/*!40000 ALTER TABLE `routes` DISABLE KEYS */;
/*!40000 ALTER TABLE `routes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stablecoins`
--

DROP TABLE IF EXISTS `stablecoins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stablecoins` (
  `stablecoin_id` int NOT NULL AUTO_INCREMENT,
  `network_id` int NOT NULL,
  `symbol` varchar(64) DEFAULT NULL,
  `address` varchar(64) DEFAULT NULL,
  `decimals` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`stablecoin_id`),
  KEY `network_id` (`network_id`),
  CONSTRAINT `stablecoins_ibfk_1` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stablecoins`
--

LOCK TABLES `stablecoins` WRITE;
/*!40000 ALTER TABLE `stablecoins` DISABLE KEYS */;
INSERT INTO `stablecoins` VALUES (1,1,'USDC','0xff970a61a04b1ca14834a43f5de4533ebddb5cc8',6,'2022-01-05 12:16:59'),(2,1,'USDT','0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9',6,'2022-01-06 12:16:59'),(3,1,'DAI','0xda10009cbd5d07dd0cecc66161fc93d7c9000da1',18,'2022-01-07 12:16:59'),(4,2,'USDC','0x750ba8b76187092b0d1e87e28daaf484d1b5273b',6,'2022-01-08 12:16:59'),(5,2,'DAI','0xda10009cbd5d07dd0cecc66161fc93d7c9000da1',18,'2022-01-09 12:16:59'),(6,3,'USDC','0x6a2d262d56735dba19dd70682b39f6be9a931d98',6,'2022-01-10 12:16:59'),(7,3,'BUSD','0x4bf769b05e832fcdc9053fffbc78ca889acb5e1e',18,'2022-01-11 12:16:59'),(8,3,'USDT','0xffffffff000000000000000000000001000007c0',6,'2022-01-12 12:16:59'),(9,4,'USDT','0x4988a896b1227218e4a686fde5eabdcabd91571f',6,'2022-01-13 12:16:59'),(10,4,'USDC','0xb12bfca5a55806aaf64e99521918a4bf0fc40802',6,'2022-01-14 12:16:59'),(11,4,'aUSDO','0x293074789b247cab05357b08052468b5d7a23c5a',8,'2022-01-15 12:16:59'),(12,5,'USDC','0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',6,'2022-01-16 12:16:59'),(13,5,'USDT.e','0xc7198437980c041c805A1EDcbA50c1Ce5db95118',6,'2022-01-17 12:16:59'),(14,5,'USDC.e','0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664',6,'2022-01-18 12:16:59'),(15,6,'USDCi','0x293074789b247cab05357b08052468b5d7a23c5a',18,'2022-01-19 12:16:59'),(16,6,'USDTi','0xc7e6d7e08a89209f02af47965337714153c529f0',18,'2022-01-20 12:16:59'),(17,7,'KUSDT','0xc7e6d7e08a89209f02af47965337714153c529f0',18,'2022-01-21 12:16:59'),(18,7,'KUSDC','0x77071ad51ca93fc90e77bcdece5aa6f1b40fcb21',18,'2022-01-22 12:16:59'),(19,8,'USDD_t','0x17f235fd5974318e4e2a5e37919a209f7c37a6d1',18,'2022-01-23 12:16:59'),(20,8,'USDT_t','0xdb28719f7f938507dbfe4f0eae55668903d34a15',6,'2022-01-24 12:16:59'),(21,8,'USDC_e','0xae17940943ba9440540940db0f1877f101d39e8b',6,'2022-01-25 12:16:59'),(22,9,'USDC','0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d',18,'2022-01-26 12:16:59'),(23,9,'USDT','0x55d398326f99059fF775485246999027B3197955',18,'2022-01-27 12:16:59'),(24,9,'BUSD','0xe9e7cea3dedca5984780bafc599bd69add087d56',18,'2022-01-28 12:16:59'),(25,10,'USDC','0x66a2a913e447d6b4bf33efbec43aaef87890fbbc',6,'2022-01-29 12:16:59'),(26,10,'DAI','0xf74195bb8a5cf652411867c5c2c5b8c2a402be35',18,'2022-01-30 12:16:59'),(27,10,'USDT','0x5de1677344d3cb0d7d465c10b72a8f60699c062d',6,'2022-01-31 12:16:59'),(28,11,'USDT','0xd567b3d7b8fe3c79a1ad8da978812cfc4fa05e75',6,'2022-02-01 12:16:59'),(29,11,'USDC','0x80b5a32e4f032b2a058b4f29ec95eefeeb87adcd',6,'2022-02-02 12:16:59'),(30,12,'cUSD','0x765DE816845861e75A25fCA122bb6898B8B1282a',18,'2022-02-03 12:16:59'),(31,12,'cEUR','0xd8763cba276a3738e6de85b4b3bf5fded6d6ca73',18,'2022-02-04 12:16:59'),(32,12,'USDT','0x88eec49252c8cbc039dcdb394c0c2ba2f1637ea0',6,'2022-02-05 12:16:59'),(33,14,'USDC','0x6963efed0ab40f6c3d7bda44a05dcf1437c44372',18,'2022-02-06 12:16:59'),(35,14,'AUSD','0xff33b107a0e2c0794ac43c3ffaf637fcea3697cf',18,'2022-02-08 12:16:59'),(36,15,'USDT','0x66e428c3f67a68878562e79a0234c1f83c208770',6,'2022-02-09 12:16:59'),(37,15,'USDC','0xc21223249ca28397b4b6541dffaecc539bff0c59',6,'2022-02-10 12:16:59'),(38,15,'TUSD','0x87efb3ec1576dec8ed47e58b832bedcd86ee186e',18,'2022-02-11 12:16:59'),(39,16,'USDT','0x79f1520268a20c879ef44d169a4e3812d223c6de',18,'2022-02-12 12:16:59'),(40,16,'USDC','0x00f0d8595797943c12605cd59bc0d9f63d750ccf',18,'2022-02-13 12:16:59'),(41,17,'USDC','0x00f0d8595797943c12605cd59bc0d9f63d750ccf',18,'2022-02-14 12:16:59'),(42,18,'USDC','0x765277eebeca2e31912c9946eae1021199b39c61',6,'2022-02-15 12:16:59'),(43,18,'USDT','0xe3f5a90f9cb311505cd691a46596599aa1a0ad7d',6,'2022-02-16 12:16:59'),(44,18,'BUSD','0x332730a4f6e03d9c55829435f10360e13cfa41ff',18,'2022-02-17 12:16:59'),(45,20,'ethUSDC','0xa06be0f5950781ce28d965e5efc6996e88a8c141',6,'2022-02-18 12:16:59'),(46,20,'htHUSD','0xf9ca2ea3b1024c0db31adb224b407441becc18bb',8,'2022-02-19 12:16:59'),(47,21,'USDE','0x04a212cf6173e3486dc8bb830927d2a5f643ce35',18,'2022-02-20 12:16:59'),(48,22,'USDC','0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',6,'2022-02-21 12:16:59'),(49,22,'DAI','0x6B175474E89094C44Da98b954EedeAC495271d0F',18,'2022-02-22 12:16:59'),(50,22,'USDT','0xdAC17F958D2ee523a2206206994597C13D831ec7',6,'2022-02-23 12:16:59'),(51,23,'USDT','0xe411107d661f722598b4956820292dc82ed1507c',6,'2022-02-24 12:16:59'),(52,24,'USDC','0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',6,'2022-02-25 12:16:59'),(53,24,'USDT','0xdac17f958d2ee523a2206206994597c13d831ec7',6,'2022-02-26 12:16:59'),(54,25,'PUSD','0xd955b4fc5f7bc5d36d826780c1207ab1c4705c9a',18,'2022-02-27 12:16:59'),(55,25,'USDT','0x8a496486f4c7cb840555bc2be327cba1447027c3',6,'2022-02-28 12:16:59'),(56,25,'USDC','0x11bbb41b3e8baf7f75773db7428d5acee25fec75',6,'2022-03-01 12:16:59'),(57,26,'axlUSDC','0x15c3eb3b621d1bff62cba1c9536b7c1ae9149b57',6,'2022-03-02 12:16:59'),(58,26,'ceUSDC','0xe46910336479f254723710d57e7b683f3315b22b',6,'2022-03-03 12:16:59'),(59,26,'ibc G-USDT','0xeceeefcee421d8062ef8d6b4d814efe4dc898265',6,'2022-03-04 12:16:59'),(60,27,'USDC','0x765277eebeca2e31912c9946eae1021199b39c61',6,'2022-03-05 12:16:59'),(61,28,'USDC','0x04068da6c83afcfa0e13ba15a6696662335d5b75',6,'2022-03-06 12:16:59'),(62,28,'fUSDT','0x049d68029688eAbF473097a2fC38ef61633A3C7A',6,'2022-03-07 12:16:59'),(63,28,'DAI','0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E',18,'2022-03-08 12:16:59'),(64,29,'USDC.e','0x2e8079e0fe49626af8716fc38adea6799065d7f7',6,'2022-03-09 12:16:59'),(65,29,'BUSD.b','0xe80eb4a234f718edc5b76bb442653827d20ebb2d',18,'2022-03-10 12:16:59'),(66,29,'USDT.e','0x0632baa26299c9972ed4d9affa3fd057a72252ff',6,'2022-03-11 12:16:59'),(67,30,'BUSD','0x6a5f6a8121592becd6747a38d67451b310f7f156',18,'2022-03-12 12:16:59'),(68,30,'fUSD','0x249be57637d8b013ad64785404b24aebae9b098b',18,'2022-03-13 12:16:59'),(69,30,'USDT','0xfadbbf8ce7d5b7041be672561bba99f79c532e10',6,'2022-03-14 12:16:59'),(70,31,'USDT','0xeceeefcee421d8062ef8d6b4d814efe4dc898265',6,'2022-03-15 12:16:59'),(71,32,'USDC','0xddafbb505ad214d7b80b1f830fccc89b60fb7a83',6,'2022-03-16 12:16:59'),(72,32,'WXDAI','0xe91d153e0b41518a2ce8dd3d7944fa863463a97d',18,'2022-03-17 12:16:59'),(73,32,'USDT','0x4ecaba5870353805a9f068101a40e0f32ed605c6',6,'2022-03-18 12:16:59'),(74,33,'USDC','0x186181e225dc1ad85a4a94164232bd261e351c33',6,'2022-03-19 12:16:59'),(75,34,'1USDC','0x985458e523db3d53125813ed68c274899e9dfab4',6,'2022-03-20 12:16:59'),(76,34,'1USDT','0x3c2b8be99c50593081eaa2a724f0b8285f5aba8f',6,'2022-03-21 12:16:59'),(77,34,'1DAI','0xef977d2f931c1978db5f6747666fa1eacb0d0339',18,'2022-03-22 12:16:59'),(78,35,'USDT','0xd16babe52980554520f6da505df4d1b124c815a7',6,'2022-03-23 12:16:59'),(79,35,'USDC','0x92a0bd4584c147d1b0e8f9185db0bda10b05ed7e',6,'2022-03-24 12:16:59'),(80,36,'DAI-HECO','0x3d760a45d0887dfd89a2f5385a236b29cb46ed2a',18,'2022-03-25 12:16:59'),(81,36,'USDT','0xa71edc38d189767582c38a3145b5873052c3e47a',18,'2022-03-26 12:16:59'),(82,36,'HUSD','0x0298c2b32eae4da002a15f36fdf7615bea3da047',8,'2022-03-27 11:16:59'),(83,37,'ioUSDC','0x3b2bf2b523f54c4e454f08aa286d03115aff326c',6,'2022-03-28 11:16:59'),(84,37,'ioUSDT','0x6fbcdc1169b5130c59e72e51ed68a84841c98cd1',6,'2022-03-29 11:16:59'),(85,37,'BUSD-bsc','0x84abcb2832be606341a50128aeb1db43aa017449',18,'2022-03-30 11:16:59'),(86,38,'KUSD-T','0x92364ec610efa050d296f1eeb131f2139fb8810e',6,'2022-03-31 11:16:59'),(87,38,'USDC','0x765277eebeca2e31912c9946eae1021199b39c61',6,'2022-04-01 11:16:59'),(88,38,'USDT','0x551a5dcac57c66aa010940c2dcff5da9c53aa53b',6,'2022-04-02 11:16:59'),(89,39,'USDC','0xfa9343c3897324496a05fc75abed6bac29f8a40f',6,'2022-04-03 11:16:59'),(90,39,'USDT','0xb44a9b6905af7c801311e8f4e76932ee959c663c',6,'2022-04-04 11:16:59'),(91,39,'DAI','0x765277eebeca2e31912c9946eae1021199b39c61',18,'2022-04-05 11:16:59'),(92,41,'oUSDT','0xcee8faf64bb97a73bb51e115aa89c17ffa8dd167',6,'2022-04-06 11:16:59'),(93,41,'oUSDC','0x754288077d0ff82af7a5317c7cb8c444d421d103',6,'2022-04-07 11:16:59'),(94,41,'KDAI','0x5c74070fdea071359b86082bd9f9b3deaafbe32b',18,'2022-04-08 11:16:59'),(95,42,'USDT','0x0039f574ee5cc39bdd162e9a88e3eb1f111baf48',18,'2022-04-09 11:16:59'),(96,42,'USDC','0x980a5afef3d17ad98635f6c5aebcbaeded3c3430',18,'2022-04-10 11:16:59'),(97,42,'DAI','0xc9baa8cfdde8e328787e29b4b078abf2dadc2055',18,'2022-04-11 11:16:59'),(98,43,'BUSD.bsc','0x24aa189dfaa76c671c279262f94434770f557c35',18,'2022-04-12 11:16:59'),(99,43,'USDC.eth','0xd86e243fc0007e6226b07c9a50c9d70d78299eb5',6,'2022-04-13 11:16:59'),(100,43,'USDT.eth','0x5fa41671c48e3c951afc30816947126ccc8c162e',6,'2022-04-14 11:16:59'),(101,44,'m.USDT','0xbb06dca3ae6887fabf931640f67cab3e3a16f4dc',6,'2022-04-15 11:16:59'),(102,44,'m.USDC','0xea32a96608495e54156ae48931a7c20f0dcc1a21',6,'2022-04-16 11:16:59'),(103,44,'m.DAI','0x4c078361fc9bbb78df910800a991c7c3dd2f6ce0',18,'2022-04-17 11:16:59'),(104,45,'sUSDC','0x42110a5133f91b49e32b671db86e2c44edc13832',6,'2022-04-18 11:16:59'),(105,45,'USDC','0xb44a9b6905af7c801311e8f4e76932ee959c663c',6,'2022-04-19 11:16:59'),(106,45,'DAI','0x6de33698e9e9b787e09d3bd7771ef63557e148bb',18,'2022-04-20 11:16:59'),(107,46,'USDC','0x818ec0a7fe18ff94269904fced6ae3dae6d6dc0b',6,'2022-04-21 11:16:59'),(108,46,'BUSD','0xa649325aa7c5093d12d6f98eb4378deae68ce23f',18,'2022-04-22 11:16:59'),(109,46,'xcUSDT','0xffffffffea09fb06d082fd1275cd48b191cbcd1d',6,'2022-04-23 11:16:59'),(110,47,'USDC','0xe3f5a90f9cb311505cd691a46596599aa1a0ad7d',6,'2022-04-24 11:16:59'),(111,47,'BUSD','0x5d9ab5522c64e1f6ef5e3627eccc093f56167818',18,'2022-04-25 11:16:59'),(112,47,'DAI','0x80a16016cc4a2e6a2caca8a4a498b1699ff0f844',18,'2022-04-26 11:16:59'),(113,48,'USDT','0xdc19a122e268128b5ee20366299fc7b5b199c8e3',6,'2022-04-27 11:16:59'),(114,48,'ceUSDC','0x81ecac0d6be0550a00ff064a4f9dd2400585fe9c',6,'2022-04-28 11:16:59'),(115,48,'USDC','0x94fbffe5698db6f54d6ca524dbe673a7729014be',6,'2022-04-29 11:16:59'),(116,49,'USDT','0xdc3af65ecbd339309ec55f109cb214e0325c5ed4',18,'2022-04-30 11:16:59'),(117,49,'USDC','0xe1ab220e37ac55a4e2dd5ba148298a9c09fbd716',18,'2022-05-01 11:16:59'),(118,50,'USDC','0xc946daf81b08146b1c7a8da2a851ddf2b3eaaf85',18,'2022-05-02 11:16:59'),(119,50,'USDT','0x382bb369d343125bfb2117af9c149795c6c65c50',18,'2022-05-03 11:16:59'),(120,50,'BUSD','0x332730a4f6e03d9c55829435f10360e13cfa41ff',18,'2022-05-04 11:16:59'),(121,51,'sUSD','0x8c6f28f2f1a3c87f0f938b96d27520d9751ec8d9',18,'2022-05-05 11:16:59'),(122,51,'vUSD','0xc84da6c8ec7a57cd10b939e79eaf9d2d17834e04',18,'2022-05-06 11:16:59'),(123,51,'USDC','0x7f5c764cbc14f9669b88837ca1490cca17c31607',6,'2022-05-07 11:16:59'),(124,52,'USDT','0x97003a080d320ea015bedba30df25e65dc32164f',6,'2022-05-08 11:16:59'),(125,52,'USDC','0x5901481e486395239434525745f37f496b41dd41',6,'2022-05-09 11:16:59'),(126,52,'DAI','0x3795c36e7d12a8c252a20c5a7b455f7c57b60283',18,'2022-05-10 11:16:59'),(127,53,'USDC','0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',6,'2022-05-11 11:16:59'),(128,53,'USDT','0xc2132D05D31c914a87C6611C10748AEb04B58e8F',6,'2022-05-12 11:16:59'),(129,53,'DAI','0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',18,'2022-05-13 11:16:59'),(130,54,'PUSD.e','0x27d789b89a441ccb6fcdb92650f1e667c965df7a',6,'2022-05-14 11:16:59'),(131,54,'USDT','0x326d041519e24fe843ce313cfb8d0f07f653b2c7',18,'2022-05-15 11:16:59'),(132,55,'USDT-R','0x73e84bfd35c3f1537a72180d1481e1eabf64b70b',18,'2022-05-16 11:16:59'),(133,57,'USDC','0xfa9343c3897324496a05fc75abed6bac29f8a40f',6,'2022-05-17 11:16:59'),(134,57,'BUSD','0x65e66a61d0a8f1e686c2d6083ad611a10d84d97a',18,'2022-05-18 11:16:59'),(135,57,'USDT','0x818ec0a7fe18ff94269904fced6ae3dae6d6dc0b',6,'2022-05-19 11:16:59'),(136,58,'bcUSDT','0xbc2f884680c95a02cea099da2f524b366d9028ba',18,'2022-05-20 11:16:59'),(137,58,'flexUSD','0x7b2b3c5308ab5b2a1d9a94d20d35ccdf61e05b72',18,'2022-05-21 11:16:59'),(138,58,'bbBUSD','0xbb1fcb08961d7fc7ab58dc608a0448aa30e66269',18,'2022-05-22 11:16:59'),(139,60,'USDC','0xe3f5a90f9cb311505cd691a46596599aa1a0ad7d',6,'2022-05-23 11:16:59'),(140,60,'USDT','0xfa9343c3897324496a05fc75abed6bac29f8a40f',6,'2022-05-24 11:16:59'),(141,61,'USDC','0xe2aa35c2039bd0ff196a6ef99523cc0d3972ae3e',6,'2022-05-25 11:16:59'),(142,62,'USDC','0x2bf9b864cdc97b08b6d79ad4663e71b8ab65c45c',6,'2022-05-26 11:16:59'),(143,62,'BUSD','0x375488f097176507e39b9653b88fdc52cde736bf',18,'2022-05-27 11:16:59'),(144,62,'USDT','0x922d641a426dcffaef11680e5358f34d97d112e1',6,'2022-05-28 11:16:59'),(145,63,'USDC','0x818ec0a7fe18ff94269904fced6ae3dae6d6dc0b',6,'2022-05-29 11:16:59'),(146,63,'USDT','0xefaeee334f0fd1712f9a8cc375f427d9cdd40d73',6,'2022-05-30 11:16:59'),(147,64,'TT-USDT','0x4f3c8e20942461e2c3bdd8311ac57b0c222f2b82',6,'2022-05-31 11:16:59'),(148,64,'TT-USDC','0x22e89898a04eaf43379beb70bf4e38b1faf8a31e',6,'2022-06-01 11:16:59'),(149,64,'TT-BUSD','0xbeb0131d95ac3f03fd15894d0ade5dbf7451d171',18,'2022-06-02 11:16:59'),(150,65,'USDC','0x4200000000000000000000000000000000000100',6,'2022-06-03 11:16:59'),(151,65,'L3USD','0x94bb580d7f99c30f125669bfaf8164d5ff6436e7',18,'2022-06-04 11:16:59'),(152,65,'fUSDT','0x7d4a600adbc6bf95fcfbc01ccee1431919752aad',6,'2022-06-05 11:16:59'),(153,66,'USDT','0x381b31409e4d220919b2cff012ed94d70135a59e',6,'2022-06-06 11:16:59'),(154,67,'BUSD','0xc111c29a988ae0c0087d97b33c6e6766808a3bd3',18,'2022-06-07 11:16:59'),(155,67,'USDT','0x01445c31581c354b7338ac35693ab2001b50b9ae',6,'2022-06-08 11:16:59'),(156,67,'USDC','0xe2c120f188ebd5389f71cf4d9c16d05b62a58993',6,'2022-06-09 11:16:59'),(157,68,'wanUSDC','0x52a9cea01c4cbdd669883e41758b8eb8e8e2b34b',6,'2022-06-10 11:16:59'),(158,68,'wanUSDT','0x11e77e27af5539872efed10abaa0b408cfd9fbbd',6,'2022-06-11 11:16:59'),(159,69,'USDC','0xe3f5a90f9cb311505cd691a46596599aa1a0ad7d',6,'2022-06-12 11:16:59');
/*!40000 ALTER TABLE `stablecoins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tokens`
--

DROP TABLE IF EXISTS `tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tokens` (
  `token_id` int NOT NULL AUTO_INCREMENT,
  `network_id` int NOT NULL,
  `name` text,
  `decimals` int NOT NULL,
  `symbol` varchar(64) DEFAULT NULL,
  `address` varchar(64) DEFAULT NULL,
  `stablecoin` bit(1) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`token_id`),
  KEY `network_id` (`network_id`),
  CONSTRAINT `tokens_ibfk_1` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tokens`
--

LOCK TABLES `tokens` WRITE;
/*!40000 ALTER TABLE `tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `network_id` int NOT NULL,
  `dex_id` int NOT NULL,
  `pair_id` int NOT NULL,
  `token_in_id` int NOT NULL,
  `token_out_id` int NOT NULL,
  `transaction_hash` varchar(255) NOT NULL,
  `block_number` decimal(38,0) DEFAULT NULL,
  `block_timestamp` decimal(38,0) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  KEY `network_id` (`network_id`),
  KEY `dex_id` (`dex_id`),
  KEY `pair_id` (`pair_id`),
  KEY `token_in_id` (`token_in_id`),
  KEY `token_out_id` (`token_out_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`network_id`) REFERENCES `networks` (`network_id`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`dex_id`) REFERENCES `dexs` (`dex_id`),
  CONSTRAINT `transactions_ibfk_3` FOREIGN KEY (`pair_id`) REFERENCES `pairs` (`pair_id`),
  CONSTRAINT `transactions_ibfk_4` FOREIGN KEY (`token_in_id`) REFERENCES `tokens` (`token_id`),
  CONSTRAINT `transactions_ibfk_5` FOREIGN KEY (`token_out_id`) REFERENCES `tokens` (`token_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-05 18:13:19
