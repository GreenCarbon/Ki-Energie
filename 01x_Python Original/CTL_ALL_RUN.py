# -----------------------------------------------------------
# Startprozedur für das Starten aller Regelprozesse
#
# -----------------------------------------------------------

from time import strptime
import time as TIME
#import mysql.connector
from CTL_Aktor_Sensor import *
import os
from datetime import *
import logging 


# Import Anweisungen für interne Klassen & Files
from INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from SQL_Tools import *
# Django Framework
from django.db import models
import sys 
import os
import django
from ki_energie import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ki_energie.settings')
django.setup()
from ki_energie.models import *

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
        
        #### Typ noch aus typ_id lesen! 
        if (typ_id == 1):
            aktor = Temperatur_Aktor(int(Id), name)
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


        
        
        