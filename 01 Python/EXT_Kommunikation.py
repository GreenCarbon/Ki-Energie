# -----------------------------------------------------------
# In dieser Datei werden alle Classen und Funktionen für die 
# externe Kommunikation mit Sensoren und Aktoren festgelegt
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
        
        
        
        
class Temp_Sensor():
    def __init__():
        pass
    
class Temp_Aktor():   
    def __init__():
        pass
        