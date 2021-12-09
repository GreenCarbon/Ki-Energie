CREATE TABLE IF NOT EXISTS `raumliste` (
  `raum_Id` int NOT NULL AUTO_INCREMENT,
  `server_name` VARCHAR(20) DEFAULT NULL,
  `etage` VARCHAR(50) DEFAULT NULL,
  `raum` VARCHAR(50) DEFAULT NULL,
  `beschreibung` VARCHAR(100) DEFAULT NULL,
  `wunsch_temperatur` DECIMAL(4,1) DEFAULT NULL,
  `wunsch_luftfeuchte` DECIMAL(4,1) DEFAULT NULL,
  `groesse_qm` DECIMAL(6,2) DEFAULT NULL,
  `raumhoehe` DECIMAL(7,2) DEFAULT NULL,
  `anzahl_sensoren` SMALLINT DEFAULT NULL,
  `nutzungsbeschreibung` varchar(100) DEFAULT NULL,
  `log_erzeugt_am` datetime DEFAULT CURRENT_TIMESTAMP,
  `log_letzte_änderung_am` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`raum_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3