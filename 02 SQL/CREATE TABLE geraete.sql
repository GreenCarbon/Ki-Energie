CREATE TABLE IF NOT EXISTS `geraete` (
  `geraete_Id` int NOT NULL AUTO_INCREMENT,
  `geraete_name` varchar(50) DEFAULT NULL,
  `geraete_art` varchar(50) DEFAULT NULL,
  `dns_name` varchar(60) DEFAULT NULL,
  `seriennummer` varchar(50) DEFAULT NULL,
  `hw_version` varchar(35) DEFAULT NULL,
  `sw_version` varchar(35) DEFAULT NULL,
  `bemerkung` varchar(100) DEFAULT NULL,
  `log_erzeugt_am` datetime DEFAULT CURRENT_TIMESTAMP,
  `log_letzte_aenderung_am` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`gerawte_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3