drop table IF EXISTS `KI_RG_GEWERK`
;
# Tabelle der Gewerke
# 
# Key-Felder sind 
# - Id

# Verknüpfte Tabellen sind
# - keine

# Rerentielle Integritäten

# Constraints


CREATE TABLE IF NOT EXISTS `KI_RG_GEWERK` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `gewerk_name` VARCHAR(100) DEFAULT ' ',
    `gewerk_ort` VARCHAR(100) DEFAULT ' ',
    `gewerk_etage` decimal DEFAULT 0,
    `log_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3