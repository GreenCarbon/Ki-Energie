# -----------------------------------------------------------
# In dieser Datei werden alle Classen und Funktionen für die 
# externe Kommunikation mit Sensoren und Aktoren festgelegt
# -----------------------------------------------------------
###
from concurrent.futures.process import _chain_from_iterable_of_lists
from time import strptime
import mysql.connector
import matplotlib.pyplot as plt
#import numpy as np
import os
import logging 
import time as TIME
import threading

from datetime import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from requests.auth import HTTPDigestAuth
import requests
import xml.etree.ElementTree as xml
# Django Framework
from django.db import models
import sys 
import os
import django
import ki_energie.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ki_energie.settings')
django.setup()
from ki_energie.models import *


import sys
import socket

# Import Anweisungen für interne Klassen & Files
from INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from SQL_Tools import *

class External_Interface() :
    __ip_addr = ''
    __svr_typ = ''
    
    def __init__(p_ip_addr, p_svr_typ):
        External_Interface.__ip_addr = p_ip_addr
        External_Interface.__svr_typ = p_svr_typ
        
        
        

#*********************************************************************************
# Aktor zur Regelung / Bestimmung der Temperaruren
#*********************************************************************************
class Temperatur_Aktor():   
    def __init__(self, id, name):
        self.name = name
        self.Aktor_Id = id
        self.con = db_conn()
        self.logger = initLogger('root')
        
# Alle Sensoren zu diesem Aktor lesen und instantiieren  
        self.ctl_list = []      
        try:
            #sql_anweisung = """SELECT * FROM ki_rg_actor_sensor 
            #    WHERE isActive = true """
            sensors = KiRgActorSensor.objects.filter(isactive = 1).filter(aktor_id= self.Aktor_Id)
            #cursor = self.con.cursor()
            #cursor.execute(sql_anweisung)
            #sql_erg = cursor.fetchall()
            sensname = ''
            #cursor.close()
            for ctl in sensors:
                Id = getattr(ctl, "id")  
                sensor = KiRgSensor.objects.filter(id = Id).first()
                sensname = getattr(sensor, "name")
                typ = getattr(sensor, "typen_id")
                sensorTyp = SensorValueTypes.objects.filter(id = Id).first()
                sensor_kategorie = getattr(sensorTyp, "kategorie")
                logging.info("Sensor " + sensname + " Typ: " + str(typ) + " hinzugefügt.")
                ##### Fehler abfagen wenn der Typ nicht existiert
                ##### Sensortyp muss zum Aktor passen
                ##### Primärer Sensorwert muss vorhanden sein
                if (sensor_kategorie == "T"): # Vorerst nur Temperatursensoren berücksichtigen
                    self.ctl_list.append(Temperatur_Sensor(Id))
# Aktor-Controller als Hintergrundprozess starten                
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()    
        except mysql.connector.Error as error:
            logging.error("Fehler beim Starten des Actor-Controllers aufgetreten: {}".format(error))
    
    def run(self):
        while 2 > 1:
            for sensor in  self.ctl_list:
                print("Aktuelle   Temperatur: ", sensor.getGeraeteArt(), " / ",  sensor.getCurrentTemperatur())
                #print("Gewünschte Temperatur: ", ctl.getTargetTemperatur())
            TIME.sleep(5)
    
# Am Ausgang für den Aktor die gewünschte Solltemperatur einstellen   
    def set_Ausgang_Temp(self, p_Temperatur):
        response = requests.get('http://192.168.20.201:2710/data/status', auth=HTTPDigestAuth('Karsten', 'Only4#Winners'))
        print(response)
        pass
    
 # Am Ausgang für den Aktor die Ventilstellung in % einstellen. 
 # 0 = geschlossen, 100 / komplett offen   
    def set_Ausgang_Ventil(self, p_Prozent):
        pass
        
    def isAktorActive(self):
        return True    
 
#*********************************************************************************
# Aktor zur Regelung / Bestimmung der Luftfeuchte
#*********************************************************************************
   
class Feuchte_Aktor():   
    def __init__(self, id, name):
        self.name = name
        self.Aktor_Id = id
        self.con = db_conn()
        self.logger = initLogger('root')
        
# Alle Sensoren zu diesem Aktor lesen und instantiieren  
        self.ctl_list = []      
        try:
            #sql_anweisung = """SELECT * FROM ki_rg_actor_sensor 
            #    WHERE isActive = true """
            sensors = KiRgActorSensor.objects.filter(isactive = 1).filter(aktor_id= self.Aktor_Id)
            #cursor = self.con.cursor()
            #cursor.execute(sql_anweisung)
            #sql_erg = cursor.fetchall()
            sensname = ''
            #cursor.close()
            for ctl in sensors:
                Id = getattr(ctl, "id")  
                sensor = KiRgSensor.objects.filter(id = Id).first()
                sensname = getattr(sensor, "name")
                typ = getattr(sensor, "typen_id")
                logging.info("Sensor " + sensname + " Typ: " + str(typ) + " hinzugefügt.")
                if (typ == 1): # Vorerst nur Temperatursensoren berücksichtigen
                    self.ctl_list.append(Temperatur_Sensor(Id))
# Aktor-Controller als Hintergrundprozess starten                
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()    
        except mysql.connector.Error as error:
            logging.error("Fehler beim Starten des Actor-Controllers aufgetreten: {}".format(error))
    
    def run(self):
        while 2 > 1:
            for ctl in  self.ctl_list:
                print("Aktuelle   Temperatur: ", ctl.getCurrentTemperatur())
                print("Gewünschte Temperatur: ", ctl.getTargetTemperatur())
                TIME.sleep(5)
    
# Am Ausgang für den Aktor die gewünschte Solltemperatur einstellen   
    def set_Ausgang_Temp(self, p_Temperatur):
        response = requests.get('http://192.168.20.201:2710/data/status', auth=HTTPDigestAuth('Karsten', 'Only4#Winners'))
        print(response)
        pass
    
 # Am Ausgang für den Aktor die Ventilstellung in % einstellen. 
 # 0 = geschlossen, 100 / komplett offen   
    def set_Ausgang_Ventil(self, p_Prozent):
        pass
        
    def isAktorActive(self):
        return True        
   
   
#*********************************************************************************
# Aktor zur Regelung / Bestimmung der Helligkeit
#*********************************************************************************
   
class Helligkeit_Aktor():   
    def __init__(self, id, name):
        self.name = name
        self.Aktor_Id = id
        self.con = db_conn()
        self.logger = initLogger('root')
        
# Alle Sensoren zu diesem Aktor lesen und instantiieren  
        self.ctl_list = []      
        try:
            #sql_anweisung = """SELECT * FROM ki_rg_actor_sensor 
            #    WHERE isActive = true """
            sensors = KiRgActorSensor.objects.filter(isactive = 1).filter(aktor_id= self.Aktor_Id)
            #cursor = self.con.cursor()
            #cursor.execute(sql_anweisung)
            #sql_erg = cursor.fetchall()
            sensname = ''
            #cursor.close()
            for ctl in sensors:
                Id = getattr(ctl, "id")  
                sensor = KiRgSensor.objects.filter(id = Id).first()
                sensname = getattr(sensor, "name")
                typ = getattr(sensor, "typen_id")
                logging.info("Sensor " + sensname + " Typ: " + str(typ) + " hinzugefügt.")
                if (typ == 1): # Vorerst nur Temperatursensoren berücksichtigen
                    self.ctl_list.append(Temperatur_Sensor(Id))
# Aktor-Controller als Hintergrundprozess starten                
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()    
        except mysql.connector.Error as error:
            logging.error("Fehler beim Starten des Actor-Controllers aufgetreten: {}".format(error))
    
    def run(self):
        while 2 > 1:
            for ctl in  self.ctl_list:
                print("Aktuelle   Temperatur: ", ctl.getCurrentTemperatur())
                print("Gewünschte Temperatur: ", ctl.getTargetTemperatur())
                TIME.sleep(5)
    
# Am Ausgang für den Aktor die gewünschte Solltemperatur einstellen   
    def set_Ausgang_Temp(self, p_Temperatur):
        response = requests.get('http://192.168.20.201:2710/data/status', auth=HTTPDigestAuth('Karsten', 'Only4#Winners'))
        print(response)
        pass
    
 # Am Ausgang für den Aktor die Ventilstellung in % einstellen. 
 # 0 = geschlossen, 100 / komplett offen   
    def set_Ausgang_Ventil(self, p_Prozent):
        pass
        
    def isAktorActive(self):
        return True          
    
#*********************************************************************************
# Aktor zur Regelung / Bestimmung der Leistung
#*********************************************************************************
   
class Leistung_Aktor():   
    def __init__(self, id, name):
        self.name = name
        self.Aktor_Id = id
        self.con = db_conn()
        self.logger = initLogger('root')
        
# Alle Sensoren zu diesem Aktor lesen und instantiieren  
        self.ctl_list = []      
        try:
            #sql_anweisung = """SELECT * FROM ki_rg_actor_sensor 
            #    WHERE isActive = true """
            sensors = KiRgActorSensor.objects.filter(isactive = 1).filter(aktor_id= self.Aktor_Id)
            #cursor = self.con.cursor()
            #cursor.execute(sql_anweisung)
            #sql_erg = cursor.fetchall()
            sensname = ''
            #cursor.close()
            for ctl in sensors:
                Id = getattr(ctl, "id")  
                sensor = KiRgSensor.objects.filter(id = Id).first()
                sensname = getattr(sensor, "name")
                typ = getattr(sensor, "typen_id")
                logging.info("Sensor " + sensname + " Typ: " + str(typ) + " hinzugefügt.")
                if (typ == 1): # Vorerst nur Temperatursensoren berücksichtigen
                    self.ctl_list.append(Temperatur_Sensor(Id))
# Aktor-Controller als Hintergrundprozess starten                
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()    
        except mysql.connector.Error as error:
            logging.error("Fehler beim Starten des Actor-Controllers aufgetreten: {}".format(error))
    
    def run(self):
        while 2 > 1:
            for ctl in  self.ctl_list:
                print("Aktuelle   Temperatur: ", ctl.getCurrentTemperatur())
                #print("Gewünschte Temperatur: ", ctl.getTargetTemperatur())
            TIME.sleep(5)
    
# Am Ausgang für den Aktor die gewünschte Solltemperatur einstellen   
    def set_Ausgang_Temp(self, p_Temperatur):
        response = requests.get('http://192.168.20.201:2710/data/status', auth=HTTPDigestAuth('Karsten', 'Only4#Winners'))
        print(response)
        pass
    
 # Am Ausgang für den Aktor die Ventilstellung in % einstellen. 
 # 0 = geschlossen, 100 / komplett offen   
    def set_Ausgang_Ventil(self, p_Prozent):
        pass
        
    def isAktorActive(self):
        return True       
    
    
#*********************************************************************************
# Sensor zur Temperaturbestimmung
#*********************************************************************************
        
class Temperatur_Sensor():
    __Hardware_Typ = "LOXONE"
    __Sensor_Typ = "STELLANTRIEB 10V"
    __IP_Addr = "192.168.20.201"
    __Port = "2710"
    __Sensor_Id = 0
    __Geraete_Art = ""
    
    def __init__(self, id):
# Der Sensor ermittelt aus der Datenbank seine Betriebs- und Kommunikationswerte   
        #self.hardware_Hersteller = "LOXONE"
        #self.Sensor_Typ = "STELLANTRIEB 10V"
        #self.IP_Addr = "192.168.20.201"
        #self.Port = "2710"
        #self.Sensor_Id = id     
        sensor = KiRgSensor.objects.filter(id = id).first()
        self.g_id = getattr(sensor, "geraete_id")
        geraet = Geraete.objects.filter(geraete_id = getattr(sensor, "geraete_id")).first()
        self.hardware_Hersteller = getattr(geraet, "hw_hersteller")
        self.geraete_Art = getattr(geraet, "geraete_art")
        self.Sensor_Typ = getattr(geraet, "geraete_art")
        self.IP_Addr = getattr(geraet, "ip_address")
        self.Port = getattr(geraet, "ip_port")
        self.get_request = getattr(geraet, "get_request")
        self.senor_Id = id
        pass
    
    def getCurrentTemperatur(self):
        r = requests.get(self.get_request)
        rtn = r.status_code
        hdr = r.headers
        value = r.text
        xmldoc = xml.fromstring(value)

        temp1 = float(xmldoc.find('./datapoint').attrib['value'].replace(",", "."))
        #print("Temperatur = %f", temp1)
        return temp1;
    
    def getGeraeteArt(self):
        return self.geraete_Art;
    
    #def getTargetTemperatur(self):
    #    r = requests.get("http://pi001/addons/xmlapi/state.cgi?datapoint_id=1467") #TA0001 von Wohnhimmer
    #    rtn = r.status_code
    #    hdr = r.headers
    #    value = r.text
    #    xmldoc = xml.fromstring(value)
    #
    #        temp1 = float(xmldoc.find('./datapoint').attrib['value'].replace(",", "."))
    #        #print("Temperatur = %f", temp1)
    #        return temp1;
    
    def getCurrentVentil(self):
        ventil = 50
        return ventil
    
    def isSensorActive(self):
        return True         
 # START <<<<<<<<
 
#Sensor1 = Temperatur_Sensor()
#while Sensor1.getTargetTemperatur() > 15:
#    print("Aktuelle   Temperatur: ", Sensor1.getCurrentTemperatur())
#    print("Gewünschte Temperatur: ", Sensor1.getTargetTemperatur())
#    TIME.sleep(1)

        