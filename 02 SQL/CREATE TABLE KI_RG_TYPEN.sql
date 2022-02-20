drop table IF EXISTS `KI_RG_TYPEN`
;
# Tabelle der AKTOR- und SENSOR-Typen für KI-Regler
# 
# Key-Felder sind 
# - Id 

# Verknüpfte Tabellen sind
# - Geraete
# - Aktoren
# - Sensoren

# Rerentielle Integritäten

# Constraints

CREATE TABLE IF NOT EXISTS `KI_RG_TYPEN` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `typ_name` VARCHAR(20) DEFAULT NULL,
    `einheit` VARCHAR(20) DEFAULT NULL,
    `min_val` DECIMAL(10,5) DEFAULT 0,
    `max_val` DECIMAL(10,5) DEFAULT 0,
    `log_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3