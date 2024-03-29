# Django Framework
from django.db import models
import sys 
import os
import django
import ki_energie.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ki_energie.settings')
django.setup()
from ki_energie.SQL_Tools import *
from ki_energie.models import *
from configparser import ConfigParser
import logging 
import os

config = ""

# Externe Parameter, welche beim Aufruf übergeben werden
class ext_params() :
    pass; 
    
 

# Hier werden alle Parameter bereitgestellt, welche über Config-File(s) beim Programmstart eingelesen werden
class config_params() :
    pass
    


# Interne Parameter, welche global für die Session angelegt werden
class int_params() :
    pass
    


class env_params() :
    pass


class tools() :
    def getCurYear() :
        return 20
    
 
# Aufruf der Systeminitialisierung. Hat alles funktioniert, wird True zurückgeliefert, bei Fehlern FALS
def SystemInit() :
    connect_database()
    p1 = os.path.abspath(".")
    parseConfig(os.path.abspath(".") + '/01_python/ki_energie/Config.ini')
    return True

def getVal(var1):
    return var1


def parseConfig(cfgFile):
    global config
    config = ConfigParser()
    print (config.read(cfgFile))
  
    print ("Sections : ", config.sections())
    sections = config.sections()
    for sec in sections: 
        print("Sections : ", sec)
        for key in config[sec]:  
            try:
                print(sec, " ", key, " " , config[sec][key])
            except:
                pass
            
def getConfigParam(p_Section, p_Key):
    global config
    return    config[p_Section][p_Key]         
    
def initLogger(name):
# Logger Config Beispiele:
#logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    #logging.warning('This is a Warning')
    #logging.basicConfig(filename='Optimizer.log', filemode='a', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    #logging.basicConfig()
    #logging.debug('Logging startet')
    #formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    #logFileName = 'Log.txt'
    #fh = logging.FileHandler(logFileName)
    #fh = RotatingFileHandler(filename=logFileName, mode="a", maxBytes=1310720, backupCount=50)
    
    #handler = logging.StreamHandler()
    #handler.setFormatter(formatter)
    
    #logger = logging.getLogger(name)
    #logger.basicConfig(filename='Optimizer.log', filemode='a', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    #logger.setLevel(logging.DEBUG)
    #logger.addHandler(handler)
    #return logger
    logfile = getConfigParam('LOG', 'logfile')    
    logging.basicConfig(filename=logfile,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
    logger = logging.getLogger(name)
    logging.info("Running Decarbonara ")

    return logger
    

    
# Damit nicht ständig Ein- und ausgeschaltet wird, kann eine Hysterese festgelegt werden.     
# Beisspiel hyst = Hysterese(21, 22)
#print(hyst.update(25))  # True bis 21 und False ab 22
    
    
class Hysterese:
    def __init__(self, temp_min, temp_max):
        self.state = False
        self.temp_min = temp_min
        self.temp_max = temp_max
        
    def update(self, temp_):
        
        if temp_ <= self.temp_min:
            self.state = True
            return self.state
     
        elif temp_ >= self.temp_max:
            self.state = False
            return self.state

        elif self.temp_min < temp_ < self.temp_max:
            self.state = False
            return self.state
 
hyst = Hysterese(25, 30)
print(hyst.update(25))  # True bis 25 und False ab 26    
    
#PID Regler, aus Internet kopiert und angepasst.    

#
# This file is part of IvPID.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# IvPID is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IvPID is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# title           :PID.py
# description     :python pid controller
# author          :Caner Durmusoglu
# date            :20151218
# version         :0.1
# notes           :
# python_version  :2.7
# ==============================================================================

"""Ivmech PID Controller is simple implementation of a Proportional-Integral-Derivative (PID) Controller in the Python Programming Language.
More information about PID Controller: http://en.wikipedia.org/wiki/PID_controller
"""
import time

class PID:
    """PID Controller
    """

    def __init__(self, P=0.2, I=0.0, D=0.0, current_time=None):

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.sample_time = 0.00
        self.current_time = current_time if current_time is not None else time.time()
        self.last_time = self.current_time

        self.clear()

    def clear(self):
        """Clears PID computations and coefficients"""
        self.SetPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0

        # Windup Guard
        self.int_error = 0.0
        self.windup_guard = 20.0

        self.output = 0.0

    def update(self, feedback_value, current_time=None):
        """Calculates PID value for given reference feedback

        .. math::
            u(t) = K_p e(t) + K_i \int_{0}^{t} e(t)dt + K_d {de}/{dt}

        .. figure:: images/pid_1.png
           :align:   center

           Test PID with Kp=1.2, Ki=1, Kd=0.001 (test_pid.py)

        """
        error = self.SetPoint - feedback_value

        self.current_time = current_time if current_time is not None else time.time()
        delta_time = self.current_time - self.last_time
        delta_error = error - self.last_error

        if (delta_time >= self.sample_time):
            self.PTerm = self.Kp * error
            self.ITerm += error * delta_time

            if (self.ITerm < -self.windup_guard):
                self.ITerm = -self.windup_guard
            elif (self.ITerm > self.windup_guard):
                self.ITerm = self.windup_guard

            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time

            # Remember last time and last error for next calculation
            self.last_time = self.current_time
            self.last_error = error

            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

    def setKp(self, proportional_gain):
        """Determines how aggressively the PID reacts to the current error with setting Proportional Gain"""
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        """Determines how aggressively the PID reacts to the current error with setting Integral Gain"""
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        """Determines how aggressively the PID reacts to the current error with setting Derivative Gain"""
        self.Kd = derivative_gain

    def setWindup(self, windup):
        """Integral windup, also known as integrator windup or reset windup,
        refers to the situation in a PID feedback controller where
        a large change in setpoint occurs (say a positive change)
        and the integral terms accumulates a significant error
        during the rise (windup), thus overshooting and continuing
        to increase as this accumulated error is unwound
        (offset by errors in the other direction).
        The specific problem is the excess overshooting.
        """
        self.windup_guard = windup

    def setSampleTime(self, sample_time):
        """PID that should be updated at a regular interval.
        Based on a pre-determined sampe time, the PID decides if it should compute or return immediately.
        """
        self.sample_time = sample_time    
        
       
class WorkValues:
   
    def __init__(self):
        self.session = "EMPTY"
        
    
    def saveWorkParam(self, app, modul, name, subname, typ, val):
        self.app = app
        self.modul = modul
        self.name = name
        self.subname = subname
        self.typ = typ 
        # Prüfen ob es den Datensatz schon gibt, wenn nicht wird er angelegt, ansonsten wird der Satz angelegt / geschrieben
        try:
            wp = Workparameter.objects.get(app = app, modul = modul, name = name, subname = subname)
        except Workparameter.DoesNotExist:
            wp = Workparameter(app = app, modul = modul, name = name, subname = subname, typ = typ, int_val = val)
            wp.save
        # Update mit neuem Wert    
        if typ == 0: #int-Value gesucht
            Workparameter.objects.filter(app = app, modul = modul, name = name, subname = subname).update(typ = typ, int_val = val)
        if typ == 1: #string-Value gesucht
           Workparameter.objects.filter(app = app, modul = modul, name = name, subname = subname).update(typ = typ, str_val = val)
        if typ == 2: #text-Value gesucht
           Workparameter.objects.filter(app = app, modul = modul, name = name, subname = subname).update(typ = typ, text_val = val)
        if typ == 3: #date-Value gesucht
           Workparameter.objects.filter(app = app, modul = modul, name = name, subname = subname).update(typ = typ, date_val = val)
        if typ == 4: #time-Value gesucht
           Workparameter.objects.filter(app = app, modul = modul, name = name, subname = subname).update(typ = typ, time_val = val)
        if typ == 5: #datetime-Value gesucht
            Workparameter.objects.filter(app = app, modul = modul, name = name, subname = subname).update(typ = typ, datetime_val = val)
            
        
        
        
    def getWorkParam(self, app, modul, name, subname, typ):
        wp = Workparameter.objects.get(app = app, modul = modul, name = name, subname = subname)
        
        if typ == 0: #int-Value gesucht
           return getattr(wp, "int_val")
        if typ == 1: #string-Value gesucht
           return getattr(wp, "str_val")
        if typ == 2: #text-Value gesucht
           return getattr(wp, "text_val")
        if typ == 3: #date-Value gesucht
           return getattr(wp, "date_val")
        if typ == 4: #time-Value gesucht
           return getattr(wp, "time_val")
        if typ == 5: #datetime-Value gesucht
           return getattr(wp, "datetime_val")
        
        return 0
            
      