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

# Import Anweisungen für interne Klassen & Files
from INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from SQL_Tools import *

SystemInit()
con = db_conn()

# Diese Werte sind vorerst statisch zum Testen. Später noch aus den Eingaben füllen
p_server_name = "PI001"
p_etage = "KG"
p_raum = "Arbeitszimmer"
p_sensorklasse = "KG_AZ_TS001"
p_name_des_wertes = "ACTUAL_TEMPERATURE"
sql_datum_von = "2021-11-14 00:00:00"
sql_datum_bis = "2021-11-16 00:00:00"

# Ergebnistabelle aufbauen
sql_anweisung = """SELECT Id,log_datum_vom, wert_num FROM import_messwerte 
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
erg_id = []
erg_datum = []
erg_zeit = []
erg_wert = []
aktval = 99999
erg_stat1 = []     #np.empty([0,4])  #ID, Datum, Zeit, Temperatur

#print(res_data)
for mwd in res_data:
      if ([mwd[2]] == aktval):
            continue        # gleiche Werte überspringen
      erg_id.append(getVal([mwd[0]]))
      erg_datum.append(getVal([mwd[1]])) 
      erg_zeit.append(getVal([mwd[1]]))
      erg_wert.append(getVal([mwd[2]]))
      aktval = getVal([mwd[2]])
print(erg_id)

# Am Ende im Array folgende Werte ermitten
#     + handelt es sich um eine Aufheiz- nzw. Abkühlphase oder um eine Plateau-Phase (obere oder untere Temperatur)
#     + die mittlere Aufheiz- - bzw. Abkühlgeschwindigkeit jeder einzelnen Phase 
#     + die höchste und niedrigste Aufheiz- bz. Abkühlgeschwindigkeit jeder Phase


# Aus den Phasen dann am Ende ermitteln
#     + Höchste Temperatur insgesamt ID, Wert und Zeit)
#     + niedrigste Temperatur insgesamt
#     + mittlere Aufheiz- und Abkühlgeschwindigkeit über alles
#     + mittlere obere und untere Temperatur
#     + Schwankung obere und untere Plateauphase (eigentlich ist nur die obere wichtig)