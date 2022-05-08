drop table importbox_fehlerlog
;

CREATE TABLE IF NOT EXISTS `importbox_fehlerlog` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `server_name` VARCHAR(20) DEFAULT NULL,
    `datei` VARCHAR(128) DEFAULT NULL,
    `fehlertext` VARCHAR(128) DEFAULT NULL,
    `satznummer` INT DEFAULT NULL,
    `datensatz` VARCHAR(2000) DEFAULT NULL,
    `log_eingelesen_am` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3