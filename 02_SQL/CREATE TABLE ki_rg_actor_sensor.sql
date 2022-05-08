drop table IF EXISTS `ki_rg_actor_sensor`
;
# Tabelle der Zurodnung von Sensoren zu Aktoren für KI-Regler
# 
# Key-Felder sind 
# - aktor_id
# - lfd

# Constraints
# jeder Aktor darf nur einmal vorkommen
# Sensoren können mehreren Aktoren zugeordnet werden

# Rerentielle Integritäten

# Constraints

CREATE TABLE IF NOT EXISTS `ki_rg_actor_sensor` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `aktor_id` BIGINT,
    `lfd` BIGINT,
    `sensor_id` BIGINT,
    `isActive` TINYINT,
    `log_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3