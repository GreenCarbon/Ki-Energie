drop table IF EXISTS `KI_RG_SENSOR`
;
# Tabelle zum Speichern der Sensoren
# Sensoren können aktuell Temperatur, Luftfeuchtigkeit, Strom, Leistung, Helligkeit sein

# Key-Felder sind 
# - Id 

# Verknüpfte Tabellen sind
# - Geraete
# - Typen
# - Raum

# Rerentielle Integritäten

# Constraints

CREATE TABLE IF NOT EXISTS `KI_RG_SENSOR` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `geraete_id` BIGINT,
    `typen_id` BIGINT,
    `name` datetime,
    `gewerk_id` BIGINT,
    `raum_id` BIGINT,
    `montageort` VARCHAR(100) DEFAULT NULL,
    `default_wert` DECIMAL(10,5) DEFAULT NULL,    
    `log_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3
  