drop table import_messwerte
;

CREATE TABLE IF NOT EXISTS `import_messwerte` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `log_datum_vom` datetime,
    `server_name` VARCHAR(20) DEFAULT NULL,
    `etage` VARCHAR(50) DEFAULT NULL,
    `raum` VARCHAR(50) DEFAULT NULL,
    `geraete_name` VARCHAR(50) DEFAULT NULL,
    `name_des_wertes` VARCHAR(50) DEFAULT NULL,
    `wert_num` DECIMAL(10,5) DEFAULT NULL,
    `wert_bit` BIT DEFAULT NULL,
    `wert_str` VARCHAR(50) DEFAULT NULL,
    `sensorklasse` VARCHAR(20) DEFAULT NULL,
    `name_sensorklasse` VARCHAR(20) DEFAULT NULL,
    `log_eingelesen_am` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3