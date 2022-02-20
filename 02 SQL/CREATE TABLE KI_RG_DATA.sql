drop table IF EXISTS `KI_RG_DATA`
;
# Tabelle zum Speichern der Lern-Daten
# Die Tabelle soll die Reglereinstellung gemäß einem mehrdimensionalen Array (später für numpy) Speichern
# Damit es über die Zeit lernfähig ist, werden nur eine maximale Anzahl an  Werten (z. Bsp. 100) gespeichert.
# Der Regler bekommt dann immer nur den statistischen Mittelwert je Punkt übermittelt. Wieviele Punkte es gibt wird im Programm festgelegt

# Key-Felder sind Raum_ID, Aktor_ID,  Sensor, Sensortyp

# Verknüpfte Tabellen sind
# - Aktor

# Rerentielle Integritäten

# Constraints

CREATE TABLE IF NOT EXISTS `KI_RG_DATA` (  
    `Id` int NOT NULL AUTO_INCREMENT,
    `sequence` BIGINT,
    `aktor_id` BIGINT,
    `learn_date` datetime DEFAULT CURRENT_TIMESTAMP,
    `soll_val` DECIMAL(10,5) DEFAULT NULL,
    `sensor_val1` DECIMAL(10,5) DEFAULT NULL,
    `sensor_val2` DECIMAL(10,5) DEFAULT NULL,
    `sensor_val3` DECIMAL(10,5) DEFAULT NULL,
    `sensor_val4` DECIMAL(10,5) DEFAULT NULL,
    `sensor_val5` DECIMAL(10,5) DEFAULT NULL,
    `regler_val1` DECIMAL(10,5) DEFAULT NULL,
    `regler_val2` DECIMAL(10,5) DEFAULT NULL,
    `regler_val3` DECIMAL(10,5) DEFAULT NULL,
    `regler_val4` DECIMAL(10,5) DEFAULT NULL,
    `regler_val5` DECIMAL(10,5) DEFAULT NULL,
    `aktor_val1` DECIMAL(10,5) DEFAULT NULL,
    `aktor_val2` DECIMAL(10,5) DEFAULT NULL,
    `aktor_val3` DECIMAL(10,5) DEFAULT NULL,
    `aktor_val4` DECIMAL(10,5) DEFAULT NULL,
    `aktor_val5` DECIMAL(10,5) DEFAULT NULL,
    `log_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3