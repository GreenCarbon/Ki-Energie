# -----------------------------------------------------------
# In dieser Datei werden alle Classen und Funktionen für die 
# externe Kommunikation mit Sensoren und Aktoren festgelegt
# -----------------------------------------------------------
###
from time import strptime
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import os
import logging 

from datetime import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from requests.auth import HTTPDigestAuth


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
        
        
        
        
class Temperatur_Sensor():
    __Hardware_Typ = "LOXONE"
    __Sensor_Typ = "STELLANTRIEB 10V"
    __IP_Addr = "192.168.20.201"
    __Port = "2710"
    
    #def __init__(self):
    #    pass
    
    def getCurrentTemperatur(self):
        response = requests.get('http://192.168.20.205/config/xmlapi/state.cgi?datapoint_id=1679')
        temperatur = 21,2
        return response;
    
    def getCurrentVentil(self):
        ventil = 50
        return ventil
    
    def isSensorActive(self):
        return True
    
class Temperatur_Aktor():   
    #def __init__(self):
    #    pass
    
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
    
 # START <<<<<<<<
 

        