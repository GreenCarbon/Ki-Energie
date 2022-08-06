from time import strptime
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import logging 

# Import Anweisungen für interne Klassen & Files
from ki_energie.INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from ki_energie.SQL_Tools import *


SystemInit()
logger = initLogger('root')
con = db_conn()

# Diese Werte sind vorerst statisch zum Testen. Später noch aus den Eingaben füllen
p_server_name = "PI001"
p_etage = "KG"
p_raum = "Arbeitszimmer"
p_sensorklasse = "KG_AZ_TS001"
p_name_des_wertes = "ACTUAL_TEMPERATURE"

sql_datum_von = "2021-11-14 00:00:00"
sql_datum_bis = "2021-11-16 00:00:00"

# Schreiben eines statistischen Records
def write_stat_rec(Id1, Id2, From_Datum, From_Time, To_Datum, To_Time, Start_val, Ende_val):
      print("Start: ", Id1, " | Ende: ", Id2, " | Von: ", From_Time, " " , To_Time, " | Temperatur von : ", Start_val , " bis : " , Ende_val)
      diff = Ende_val - Start_val
      phase = "Phase"
      cursor = con.cursor()
      try:
            sql_anweisung = """INSERT INTO AUW_StatKurven (id_Messwert_1, id_Messwert_2, start_time, end_time, wert_num_1, wert_num_2, wert_diff, phase)
                               VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
                               
            sql_werte = (Id1, Id2, From_Time, To_Time, Start_val, Ende_val, diff, phase)

            db_ergebnis = cursor.execute(sql_anweisung, sql_werte)
            con.commit()
            
      except mysql.connector.Error as error:
            print("Fehler beim Schreiben in die AUW_StatKurven: {}".format(error))
            logging.error("Fehler beim Schreiben in die AUW_StatKurven: {}".format(error))

      return

############ Einstieg Hauptprogramm

# Ergebnistabelle aufbauen
sql_anweisung = """SELECT Id,log_datum_vom, wert_num FROM ki_energie_importmesswerte 
                        WHERE server_name = %s AND etage = %s AND raum = %s AND sensorklasse = %s AND name_des_wertes = %s 
                              AND log_datum_vom >= DATE(%s) AND log_datum_vom < DATE(%s)
                        ORDER BY Id, log_datum_vom"""
sql_werte = (p_server_name, p_etage, p_raum, p_sensorklasse, p_name_des_wertes, sql_datum_von, sql_datum_bis)
             
cursor = con.cursor()
cursor.execute(sql_anweisung, sql_werte)
res_data = cursor.fetchall()
cursor.close()

# Jetzt alle Anstiegs- und Abkühlkurven ermitteln. Dabei wird wie folgt vorgegangen:
# - Ab dem ersten Datensatz wird die erste Temperatur gemerkt
# - nächste Temperatur höher oder niedriger ? Schalter für fallende oder steigenden Kurve ermitteln
# - so lange bis Temperatur wieder in die andere Richtung geht. 
# - in Array speichern der folgenden Werte
#   + ID, Temperatur und Zeit des ersten Datensatzes
#   + ID, Temperatur und Zeit des letzten Datensatzes

k_t_max = 100,0
k_t_min = -100,0
t_max = k_t_max
t_min = k_t_min
sel1_id = []
sel1_datum = []
sel1_zeit = []
sel1_wert = []
aktval = 99999
sel1_stat1 = []     #np.empty([0,4])  #ID, Datum, Zeit, Temperatur

#print(res_data)
for mwd in res_data:
      if ([mwd[2]] == aktval):
            continue        # gleiche Werte überspringen
      sel1_id.append(getVal(mwd[0]))
      sel1_datum.append(getVal(mwd[1])) 
      sel1_zeit.append(getVal(mwd[1]))
      sel1_wert.append(getVal(mwd[2]))
      aktval = getVal(mwd[2])
#print(sel1_id)

# Am Ende im Array folgende Werte ermitten
#     + handelt es sich um eine Aufheiz- nzw. Abkühlphase oder um eine Plateau-Phase (obere oder untere Temperatur)
#     + die mittlere Aufheiz- - bzw. Abkühlgeschwindigkeit jeder einzelnen Phase 
#     + die höchste und niedrigste Aufheiz- bz. Abkühlgeschwindigkeit jeder Phase
i = 0
going_up = True
going_down = False
upper_Plateau = True
lower_Plateau = False
sel2_stat = []
high_value = -100
low_value = 100
start_value = 100
from_Id = 0
from_datum = "*START"
from_zeit = "*START"
i = 1
# Nur wenn es mehr als einen Wert gibt, dann entsprechend der ersten beiden Werte alles belegen 
if (len(sel1_id) > 1):
      from_Id = sel1_id[0]
      low_value = sel1_wert[0]
      start_value = sel1_wert[0]
      high_value = sel1_wert[0]
      from_datum = sel1_datum[0]
      from_zeit = sel1_zeit[0]
      if (sel1_wert[1] < sel1_wert[0]):
            going_down = True
            going_up = False
            
            
# Durchgehen der Werte ab der zweiten Zeile (i=1)
i = 0     

while i < len(sel1_id) :
      i+=1
      
      if ((i + 2) == len(sel1_id)):      # Letzte zeile erreicht   
            write_stat_rec(from_Id, sel1_id[i], from_datum, from_zeit, sel1_datum[i], sel1_zeit[i], start_value, sel1_wert[i])    
            break    
     
      if (going_up and sel1_wert[i] > sel1_wert[i-1]):  # Weiter steigend
            high_value = sel1_wert[i]
            continue
         
      if (going_down and sel1_wert[i] < sel1_wert[i-1]):  # Weiter fallend
            low_value = sel1_wert[i]      
            continue
      
      if (going_up and sel1_wert[i] < sel1_wert[i-1]):  # Wechsel von steigend nach fallend
            write_stat_rec(from_Id, sel1_id[i], from_datum, from_zeit, sel1_datum[i], sel1_zeit[i], start_value, sel1_wert[i])
            start_value = sel1_wert[i]
            high_value = sel1_wert[i]
            from_Id = sel1_id[i]
            from_datum = sel1_datum[i]
            from_zeit = sel1_zeit[i]
            going_down = True
            going_up = False
            continue
            
      if (going_down and sel1_wert[i] > sel1_wert[i-1]):  # Wechsel von fallend nach steigend
            write_stat_rec(from_Id, sel1_id[i], from_datum, from_zeit, sel1_datum[i], sel1_zeit[i], start_value, sel1_wert[i])
            start_value = sel1_wert[i]
            low_value = sel1_wert[i]
            from_Id = sel1_id[i]
            from_datum = sel1_datum[i]
            from_zeit = sel1_zeit[i]
            going_up = True
            going_down =False
            continue
            
      
# Aus den Phasen dann am Ende ermitteln
#     + Höchste Temperatur insgesamt ID, Wert und Zeit)
#     + niedrigste Temperatur insgesamt
#     + mittlere Aufheiz- und Abkühlgeschwindigkeit über alles
#     + mittlere obere und untere Temperatur
#     + Schwankung obere und untere Plateauphase (eigentlich ist nur die obere wichtig)

