# -----------------------------------------------------------
# Analyseprozess für alle Daten in Tabelle ImportMesswerte
# Dazu werden ALLE Messwerte durchgegangen und ausgewertet
# Heizkurven werden ermittelt und mit den Vorgabewerten verglichen
# Sollten Ergebnisse bereits existieren, so werden diese nicht nochmals
# fortgeschrieben
# -----------------------------------------------------------

from time import strptime
import time as TIME
#import mysql.connector
import os
from datetime import *
import logging

from sympy import cancel, false 




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
from ki_energie.KI_Objects import *
# Import Anweisungen für interne Klassen & Files
from ki_energie.INT_Classes import *
from ki_energie.models import *

SystemInit()
logger = initLogger('root')
con = db_conn()

#----------------------------------------------------------------
# Lokale Funktionsdefinitionen
#----------------------------------------------------------------
# Ermittlung und Rückgabe der der ID's aus der Tabellel KIRGTYPEN. ACHTUNG: Der Inhalt dieser Tabelle ist fix und sollte nicht verändert, nur ergänzt werden ! 
def getValueType(sensorname):
    
    if sensorname == "ACTUAL_TEMPERATURE":
        return 1
    if sensorname == "SET_POINT_TEMPERATURE":
        return 2
    if sensorname == "HUMIDITY":
        return 3
    if sensorname == "ILLUMINATION":
        return 4
    if sensorname == "CURRENT_ILLUMINATION":
        return 4
    if sensorname == "HIGHEST_ILLUMINATION":
        return 5
    if sensorname == "LOWEST_ILLUMINATION":
        return 6
    if sensorname == "CURRENT":
        return 7
    if sensorname == "MOTION":
        return 8
    
    return  99 # Default Rückgabe ist 99 = Unbekannter Wertetyp


#----------------------------------------------------------------
# Primäre Schleife: Alle Messwerte lesen

logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
################
# Die folgenden Definitionen müssen später durch einen externen Aufruf getätigt werden!
################
run_import = True
run_analysis = False
run_controller = False
param_kunde = 2
param_gebaeude = 1
################
################
# =============================================================
# Start der Action Controller Regelung
# =============================================================

if run_import:

# Erster Durchlauf: Ermittlung der Perioden und schreiben in Erg_Analyse
# Bei 2 aufeinander folgenden messwerden wird der jeweils vorhergehende eliminiert, es sei denn es handelt sich um eine Richtungsumkehr
# Richtungsumkehr muss innerhalb von 15 min definitiv erfolgt und durch 2 Messwerte bestätigt werden    
    #xx = RaumlisteInd1.objects.only('raum')   
    #for r in xx:
    #    print(getattr(r, 'raum'))
    erg_id = ErgAnalyse.objects.values('id')
    wp = WorkValues()
    from_id = wp.getWorkParam("Auswertung", "ImportMesswerte", "Status_id", "End" , 0)
    from_id = 0 #### >>>>> MUSS WIEDER RAUS!!!
    nbr = wp.getWorkParam("Auswertung", "ImportMesswerte", "Status_id", "Records" , 0)
    messwerte = ImportMesswerte.objects.filter(id__gt=from_id).order_by('server_name', 'etage', 'raum', 'geraete_name', 'log_datum_vom')[:nbr]
    first = True
    write = False
    server_name = ""
    geraete_name = ""
    etage_name = ""
    raum = 0
    wert_bit = 0
    wert_num = 0.0
    wert_str = ""
    von_datum = datetime.now()
    # curdate = datetime.now()
    # x = str(curdate)
    # mwadd.von_date_time = x
#    print(messwerte)
# Nur Messwerte übertragen wo der Wert sich geändert hat.     
    i = 0
    lfd_id = 0
    for mw in messwerte:
        i+=1
        if i==100:
            wp.saveWorkParam("Auswertung", "ImportMesswerte", "Status_id", "End" , 0, lfd_id)
            i= 0
        write = False
        if (first):
            first = False
            write = True
            von_datum = getattr(mw, "log_datum_vom")
        else:
            if server_name == getattr(mw, "server_name") \
                and raum == getattr(mw, "raum") \
                and geraete_name == getattr(mw, "geraete_name") \
                and etage_name == getattr(mw, "etage") \
                and wert_bit == getattr(mw, "wert_bit") \
                and wert_str == getattr(mw, "wert_str") \
                and wert_num == getattr(mw, "wert_num"):
                write = false
            else:
                write = True    
# Aktuelle Werte merken          
        if write:
            mwadd = ErgAnalyse(kunde_id = param_kunde, server_id = 0, gebaeude_id = param_gebaeude, etage_id = 0, raum_id = 0, periode = 0 , periode_typ = 0, \
            wert_typ = 0, tgt_val = 0, min_val = 0, max_val = 0, rise_time= 0, max_rise = 0, min_rise = 0, \
            goodness = 0, optimum_percent = 0)
            mwadd.messwert_id = getattr(mw, "id")
            #raum_id = KI_Raum().get_or_create_by_name(getattr(mw, "raum"))
            #try:
            #    r_name = getattr(mw, "raum")
            #    rl = Raumliste.objects.get(raum = r_name)
            #except Raumliste.DoesNotExist:
            #    rl1 = Raumliste.objects.order_by('-id').first()
            #    new_id = getattr(rl1, "id") + 1
            #    logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #    rl = Raumliste(id = new_id, server_name = "PI???", etage = "???", raum = getattr(mw, "raum"), beschreibung = "*AUTOMATISCHE ANLAGE!", log_erzeugt_am = logdat)
            #    rl.save()
            etage_id = KI_Etage().get_or_create_by_name(getattr(mw, "etage"), param_gebaeude)
            server_id = KI_Server().get_or_create_by_name(getattr(mw, "server_name"))
            
            mwadd.raum_id = KI_Raum().get_or_create_by_name(getattr(mw, "raum"), param_kunde, param_gebaeude, server_id, etage_id )
            mwadd.server_id = server_id
            mwadd.etage_id = etage_id
            
            xx = getattr(mw, "geraete_name")
            mwadd.geraete_id = KI_Geraet().get_or_create_by_serialnumber(getattr(mw, "geraete_name"))
            mwadd.wert_typ = getValueType(getattr(mw, "name_des_wertes"))
            mwadd.von_date_time = von_datum
            mwadd.bis_date_time = getattr(mw, "log_datum_vom")
            mwadd.log_datum_vom = str(datetime.now())
            mwadd.save()    
            lfd_id = mwadd.id
            von_datum = getattr(mw, "log_datum_vom")      
        Id = getattr(mw, "id")  
        server_name = getattr(mw, "server_name") 
        #raum = getattr(mw, "raum")
        raum = 0

        geraete_name =getattr(mw, "geraete_name")  
        etage_name =getattr(mw, "etage")  
        wert_bit =getattr(mw, "wert_bit") 
        wert_str =getattr(mw, "wert_str") 
        wert_num =getattr(mw, "wert_num") 
        #von_datum = getattr(mw, "log_datum_vom"
#        print(Id, " ", server_name, " ", raum, " ", geraete_name,  " ", wert_str,  " ",wert_num)
#--- Ende Datenübernahme, letzte ID speichern sofern etwas verarbeitet wurde.        
    if lfd_id > 0:
        wp.saveWorkParam("Auswertung", "ImportMesswerte", "Status_id", "End" , 0, lfd_id)
#except:
#    logging.error("Fehler beim Import aufgetreten!")        

# =============================================================
# Start der Analyse der importierten Eregbnistabelle
# =============================================================
if run_analysis:
    try: 
        messwerte = ErgAnalyse.objects.order_by('server_name', 'raum', 'geraete_name', 'log_datum_vom')[:nbr]
        first = True
        write = False
        server_name = ""
        geraete_name = ""
        i = 0
        lfd_id = 0
        for mw in messwerte:
            if getattr(mw, "periode") > 0:   # Wenn Periode bereits ermittelt dann nächsten Wert
                continue
            write = False
            if (first):
                first = False
                write = True
            else:
                
# Wechsel von Etage / Raum / Gerät ?? Dann letzte Phase wegschreiben und erste Phase für neuen Bereich merken                
# Letzten Wert merken
# die nächsten 2 Werte lesen, wenn diese auf- oder abwärts zeigen dann den dritten Wert lesen und bestägigen 
# Bei keiner Bestätigung ist es eine Plateauphase
# Prüfen ob Periodenwechsel vorliegt, wenn ja dann Anfangswerte der neuen Periode merken 
# Wenn es nicht die erste Periode ist, dann die Endewerte der letzten Periode schreiben
#   - dazu die Anstiegs bzw. Abfallkurve ermitteln
#   - größten und kleinsten Anstieg
#   - bei Plateauphase niedrigste, höchsten und Mittelwert ermitteln
                if server_name == getattr(mw, "server_name") \
                    and raum == getattr(mw, "raum") \
                    and geraete_name == getattr(mw, "geraete_name") \
                    and wert_bit == getattr(mw, "wert_bit") \
                    and wert_str == getattr(mw, "wert_str") \
                    and wert_num == getattr(mw, "wert_num"):
                    write = false
                else:
                    write = True    
                mwadd.save()    
                lfd_id = mwadd.id
                von_datum = getattr(mw, "log_datum_vom")      
            Id = getattr(mw, "id")  
            server_name = getattr(mw, "server_name") 
            #raum = getattr(mw, "raum")
            raum = 0

    except:
        logging.error("Fehler bei der Analse !") 
            
    logging.info("Analyse beendet.")
    logging.info("=====================================")
        


# =============================================================
# Start der Action Controller Regelung
# =============================================================
if run_controller:
    try: 
        actors = KiRgActor.objects.filter(isactive = 1).filter(id= 1)
        for ctl in actors:
            Id = getattr(ctl, "id")  
            name = getattr(ctl, "name") 
            typ_id = getattr(ctl, "typen_id") # Type = 1 = Temperatursteuerung
            actor_typ = getattr(KiRgTypen.objects.filter(id = Id).first(), "typ_name")
            #### Fehler abfangen wenn der Typ nicht existiert 
            
            if (typ_id == 1):
                aktor = Temperatur_Aktor(int(Id), name)
                ctl.append(aktor)
                logging.info(actor_typ + " Controller " + name + " gestartet.")
            if (typ_id == 2):
                aktor = Feuchte_Aktor(int(Id), name)
                ctl.append(aktor)
                logging.info(actor_typ + " Controller " + name + " gestartet.")
            if (typ_id == 3):
                aktor = Helligkeit_Aktor(int(Id), name)
                ctl.append(aktor)
                logging.info(actor_typ + " Controller " + name + " gestartet.")
            if (typ_id == 4):
                aktor = Leistung_Aktor(int(Id), name)
                ctl.append(aktor)
                logging.info(actor_typ + " Controller " + name + " gestartet.")    
            

    except mysql.connector.Error as error:
            logging.error("Fehler beim Starten der Controller aufgetreten: {}".format(error))
            
    logging.info("Folgende Controller sind jetzt aktiv:")
    logging.info("=====================================")
    for ctl in ctl:
        logging.info(">>>> : " + str(ctl.Aktor_Id) +  " / " +  ctl.name)

# Endlosschleife, alles andere erledigen die Hintergrundprozesse    
    while 2 > 1:    
        TIME.sleep(60)



        
        
        