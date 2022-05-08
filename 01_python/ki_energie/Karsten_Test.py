# -*- coding: utf-8 -*-
"""

PI plus D-T1 Regler
Created on 15.4. 2019
@author: philippsen
"""

import numpy as np
import control
from   control.matlab import *
import matplotlib.pyplot as plt

Kp= 2.0    #  Reglerverstärkung
Tn = 1.5    # Nachstellzeit
Tv = 0.5    # Vorhaltzeit
VV = 5      #  Vorhaltverstärkung

Zpi  = np.array([Kp*Tn , Kp ])
Npi  = np.array([ Tn, 0])
Zdt1  = np.array([Kp*Tv , 0])
Ndt1  = np.array([Tv/VV , 1])
t = np.arange(0,10,0.05)
Gpi = tf(Zpi,Npi)
ypi, t = control.matlab.step(Gpi,t)

Gdt1 = tf(Zdt1,Ndt1)
ydt, tt = control.matlab.step(Gdt1,t)
fig, ax1 = plt.subplots()

ax1.plot(tt, ypi+ydt, "b") 
ax1.set_ylabel('Stellgröße', color="blue", fontsize=14) 
plt.grid()
ax2 = ax1.twinx() 
ax2.plot(tt, ydt, "r") 
ax2.set_ylabel('D-Anteil', color="red", fontsize=14) 
ax1.set_xlabel('t [s]', fontsize=12) 
ax1.set_title('PID-T1 - Regler', fontsize=12)
x = 1
## Anderer PID Regler : https://onion.io/2bt-pid-control-python/