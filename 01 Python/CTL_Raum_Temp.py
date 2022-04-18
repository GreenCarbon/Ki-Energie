#
# 
# AKTUELL KEINE VERWENDUNG !!!!!!!!
#
# ## -----------------------------------------------------------
# Controller für Raumtemperatur
# Übernimmt die komplette Raumtemperatursteuerung 
# -----------------------------------------------------------

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
from CTL_Aktor_Sensor import *

# Import Anweisungen für interne Klassen & Files
from INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from SQL_Tools import *

SystemInit()
logger = initLogger('root')
con = db_conn()

S_temp = Temperatur_Sensor()
xx = S_temp.getCurrentTemperatur()
logging.error(xx)
#A_temp = Temperatur_Aktor()
#A_temp.set_Ausgang_Temp(21)




class Control_Raum_Temp() :
    __server = ''
    __raum = ''
    __starttime = ''
    __solltemp = 0
    __isttemp = 0
    
    def __init__(p_server, p_raum, p_sensor, p_aktor):
        Control_Raum_Temp.__server = p_server
        Control_Raum_Temp.__raum = p_raum
        Control_Raum_Temp.__server = p_sensor
        Control_Raum_Temp.__server = p_aktor
        
        
        