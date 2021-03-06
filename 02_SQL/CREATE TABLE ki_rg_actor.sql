drop table IF EXISTS `ki_rg_actor`
;
# Tabelle der Aktoren für KI-Regler
# 
# Key-Felder sind 
# - Id

# Verknüpfte Tabellen sind
# - Geraete
# - Gewerke
# - Raum

# Rerentielle Integritäten

# Constraints

CREATE TABLE IF NOT EXISTS `KI_RG_AKTOR` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `geraete_id` BIGINT,
    `typen_id` BIGINT,
    `name` VARCHAR(100) DEFAULT NULL,
    `gewerk_id` BIGINT,
    `raum_id` BIGINT,
    `montageort` VARCHAR(100) DEFAULT NULL,
    `default_wert` DECIMAL(10,5) DEFAULT NULL,    
    `log_date` datetime DEFAULT CURRENT_TIMESTAMP,
    `isActive` TINYINT,
  PRIMARY KEY (`Id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3