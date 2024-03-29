# -----------------------------------------------------------
# Startprozedur für das Starten aller Regelprozesse
#
# -----------------------------------------------------------

from time import strptime
import time as TIME
#import mysql.connector
import os
from datetime import *
import logging 


# Import Anweisungen für interne Klassen & Files
from ki_energie.INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from ki_energie.SQL_Tools import *
# Django Framework
from django.db import models
import sys 
import os
import django
import ki_energie.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ki_energie.settings')
django.setup()
from ki_energie.models import *
from CTL_Aktor_Sensor import *

SystemInit()
logger = initLogger('root')
con = db_conn()


# Primäre Schleife: Alle aktiven Aktoren lesen und für jeden Aktor je nach Typ einen Controller starten
ctl_list = []
try:
    #sql_anweisung = """SELECT * FROM ki_rg_actor 
    #                    WHERE isActive = true"""
   
    #cursor = con.cursor()
    #cursor.execute(sql_anweisung)
    #sql_erg = cursor.fetchall()
    #cursor.close()
    actors = KiRgActor.objects.filter(isactive = 1).filter(id= 1)
    for ctl in actors:
        Id = getattr(ctl, "id")  
        name = getattr(ctl, "name") 
        typ_id = getattr(ctl, "typen_id") # Type = 1 = Temperatursteuerung
        actor_typ = getattr(KiRgTypen.objects.filter(id = Id).first(), "typ_name")
        #### Fehler abfangen wenn der Typ nicht existiert 
        
        if (typ_id == 1):
            aktor = Temperatur_Aktor(int(Id), name)
            ctl_list.append(aktor)
            logging.info(actor_typ + " Controller " + name + " gestartet.")
        if (typ_id == 2):
            aktor = Feuchte_Aktor(int(Id), name)
            ctl_list.append(aktor)
            logging.info(actor_typ + " Controller " + name + " gestartet.")
        if (typ_id == 3):
            aktor = Helligkeit_Aktor(int(Id), name)
            ctl_list.append(aktor)
            logging.info(actor_typ + " Controller " + name + " gestartet.")
        if (typ_id == 4):
            aktor = Leistung_Aktor(int(Id), name)
            ctl_list.append(aktor)
            logging.info(actor_typ + " Controller " + name + " gestartet.")    
        

except mysql.connector.Error as error:
        logging.error("Fehler beim Starten der Controller aufgetreten: {}".format(error))
        
logging.info("Folgende Controller sind jetzt aktiv:")
logging.info("=====================================")
for ctl in ctl_list:
    logging.info(">>>> : " + str(ctl.Aktor_Id) +  " / " +  ctl.name)
    

# Endlosschleife, alles andere erledigen die Hintergrundprozesse    
while 2 > 1:    
    TIME.sleep(60)


        
        
        