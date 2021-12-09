CREATE TABLE IF NOT EXISTS `geraete2kunde` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `geraete_Id` INT COMMENT 'Primary Key von Geräte',
    `kunde_Id` INT COMMENT 'Primary Key von Kunde',
    `raum` VARCHAR(50) DEFAULT NULL,
    `bemerkung` VARCHAR(100) DEFAULT NULL,
    `log_erzeugt_am` datetime DEFAULT CURRENT_TIMESTAMP,
    `log_letzte_aenderung_am` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3