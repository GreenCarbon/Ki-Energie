#from typing import Collection
#from _typeshed import Self
from time import strptime
import mysql.connector
#import matplotlib.pyplot as plt
#import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2Tk
#import numpy as np
import os
from datetime import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import logging 
 
# Import Anweisungen für interne Klassen & Files
from ki_energie.INT_Classes import *
from ki_energie.SQL_Tools import *

SystemInit()
con = db_conn()

m_datum_von = ''
m_datum_bis = ''

def button_action():

    p_server_name = p1.get()
    p_etage = p2.get()
    p_raum = p3.get()
    p_sensorklasse = p4.get()
    p_name_des_wertes = p5.get()
    p_datum_von = p6.get()
    p_datum_bis = p7.get()

    fehler.set('')

    if p_server_name == '':
        fehler.set('Bitte wählen Sie einen gültigen Server aus.')
    elif p_etage == '':
        fehler.set('Bitte wählen Sie einen gültige Etage aus.')
    elif p_raum == '':
        fehler.set('Bitte wählen Sie einen gültigen Raum aus.')
    else:
        #x_grafik = 
        graf_erzeugen(p_server_name, p_etage, p_raum, p_sensorklasse, p_name_des_wertes, p_datum_von, p_datum_bis)
        #n_grafik = ImageTk.PhotoImage(Image.open(x_grafik))
        #l_grafik .configure(image=n_grafik)
        #l_grafik.image = n_grafik
        #l_grafik.place(x=530, y=50)
        #i_fenster.geometry('1210x570+10+10')

        #i_fenster.destroy()


def call_cb_etage(event):
    sql_etage = event.widget.get()
    #fehler.set('Ich bin hier')
    sql_anweisung = """SELECT DISTINCT raum FROM ki_energie_importmesswerte
                       WHERE etage = %s
                       ORDER BY raum"""
    sql_werte = (sql_etage,)
    a_raum = db_select(sql_anweisung, sql_werte, "ki_energie_importmesswerte")
    cb_raum['values'] = a_raum
    if len(a_raum) == 1:
        cb_raum.current(0)


def graf_erzeugen(p_server_name, p_etage, p_raum, p_sensorklasse, p_name_des_wertes, p_datum_von, p_datum_bis):

    try:
        sql_time_min = time.min.__str__()
        sql_datum_von =  p_datum_von + ' ' + sql_time_min
        plus_1tag = timedelta(1)
        dat_datum_bis = datetime.strptime(p_datum_bis, "%Y-%m-%d") 
        sql_datum_bis = dat_datum_bis + plus_1tag
        sql_anweisung = """SELECT * FROM ki_energie_importmesswerte 
                        WHERE server_name = %s AND etage = %s AND raum = %s AND sensorklasse = %s AND name_des_wertes = %s 
                              AND log_datum_vom >= DATE(%s) AND log_datum_vom < DATE(%s)
                        ORDER BY log_datum_vom"""
        sql_werte = (p_server_name, p_etage, p_raum, p_sensorklasse, p_name_des_wertes, sql_datum_von, sql_datum_bis)
             
        cursor = con.cursor()
        cursor.execute(sql_anweisung, sql_werte)
        sql_ergebnis = cursor.fetchall()
        cursor.close()
    
        xwerte_init = []
        ywerte_init = []
        xwerte = []
        ywerte = []
        for daten in sql_ergebnis:
            xwerte_init = [daten[1]]
            xwerte.append(xwerte_init)
            ywerte_init = [daten[7]]
            ywerte.append(ywerte_init)

    except mysql.connector.Error as error:
        fehler.set("Fehler beim Lesen der Tabelle ki_energie_importmesswerte: {}".format(error))

    #fig = Figure(figsize=(7, 15), dpi=110)
    #plot1 = fig.add_subplot(1,1,1)
    
    global m_datum_von
    global m_datum_bis
    if (m_datum_von != p_datum_von) or (m_datum_bis != p_datum_bis):
        m_datum_von = p_datum_von
        m_datum_bis = p_datum_bis
        #fig.clf()
        #plt.clf()
        #i_fenster.geometry('510x570+10+10')

    i_fenster.geometry('1210x570+10+10')

    #rahmen1 = Frame(master=i_fenster, bg='magenta')
    #rahmen1.pack(side='right', padx='35')

    dataPlot.clf()
    dataPlot.plot(xwerte, ywerte)
    dataPlot.set_xlabel('Zeit-Achse')
    dataPlot.set_ylabel('Temperatur')
    
    #canvas = FigureCanvasTkAgg(fig, master=i_fenster)    
    #canvas.draw()
    #canvas.get_tk_widget().pack(side='right', padx='35')
    
    #plt.plot(xwerte, ywerte) #, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    #plt.step(xwerte, ywerte) #, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    #plt.bar(xwerte, ywerte)
    #plt.xlabel('Zeit-Achse')
    #plt.ylabel('Temperatur')
    #s_grafik = aktuelle_zeit + '_' + p_server_name + '_' + p_etage + '_' + p_raum + '.png'
    #plt.figure()
    #plt.savefig(s_grafik)
    #plt.show()

    #n_grafik = ImageTk.PhotoImage(Image.open(x_grafik))
    #l_grafik .configure(image=n_grafik)
    #l_grafik.image = n_grafik
    #l_grafik.place(x=530, y=50)
    #ci_fenster.geometry('1210x570+10+10')

    #i_fenster.destroy()
 
 
    
    return #s_grafik

class myPlot:
    def generatePlot(self):
        f = Figure(figsize=(7,15), dpi=110)

        # Setup subplots
        self.subplot1=f.add_subplot(2,1,1)

        # Show plots
        self.dataPlot = FigureCanvasTkAgg(f, master=i_fenster)
        self.dataPlot.show()
        self.dataPlot.get_tk_widget().pack(side=RIGHT, padx='35', fill=BOTH, expand=1)


def db_select(p_sql_anweisung, p_sql_werte, p_sql_tabelle):
    
    r_sql_ergebnis = None
    try:
        cursor = con.cursor()
        cursor.execute(p_sql_anweisung, p_sql_werte)
        r_sql_ergebnis = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as error:
        print("Fehler beim Lesen der Tabelle " + p_sql_tabelle + " : {}".format(error))
    
    return r_sql_ergebnis


aktuelle_zeit = datetime.now().strftime('%Y%m%d-%H%M%S')  # Format = 20211109-131856

cursor = con.cursor()

i_fenster = tk.Tk()
i_fenster.title('Eingaben für die Auswertungsgrafik')
i_fenster.geometry('510x570+10+10')

#myPlot.generatePlot()
f = Figure(figsize=(7,15), dpi=110)

# Setup subplots
subplot1=f.add_subplot(2,1,1)

# Show plots
dataPlot = FigureCanvasTkAgg(f, master=i_fenster)
#dataPlot.show()
dataPlot.get_tk_widget().pack(side=RIGHT, padx='35', fill=BOTH, expand=1)


#arbeits_pfad = os.getenv('HOME') + '/Alles/Kunden/Decarbonara/01_Workspace_GIT/01_python'
p1 =  os.path.abspath(os.getcwd())
arbeits_pfad = os.path.abspath(os.getcwd()) + '/01_python/ki_energie'
os.chdir(arbeits_pfad)

l_eckdaten = Label(i_fenster, text="Eckdaten", anchor='w', font=('Arial', 18)).place(x=20, y=50, width=100, height=24)
l_server_name = Label(i_fenster, text="Server: ", anchor='w').place(x=20, y=90, width=100, height=24)
l_etage = Label(i_fenster, text="Etage: ", anchor='w').place(x=20, y=120, width=100, height=24)
l_raum = Label(i_fenster, text="Raum: ", anchor='w').place(x=20, y=150, width=100, height=24)
l_sensorklasse = Label(i_fenster, text="Sensorklasse: ", anchor='w').place(x=20, y=180, width=100, height=24)
l_name_des_wertes = Label(i_fenster, text="Wert: ", anchor='w').place(x=20, y=210, width=100, height=24)

l_zeitraum = Label(i_fenster, text="Zeitraum", anchor='w', font=('Arial', 18)).place(x=20, y=270, width=100, height=24)
l_zeitraum_von = Label(i_fenster, text="Datum von: ", anchor='w').place(x=20, y=310, width=100, height=24)
l_zeitraum_bis = Label(i_fenster, text="Datum bis: ", anchor='w').place(x=20, y=350, width=100, height=24)

fehler = tk.StringVar()
l_fehlerzeile = Label(i_fenster, text="Fehlerblock", fg='red', textvariable=fehler, anchor='w').place(x=20, y=480, width=400, height=24)

#s_grafik = ImageTk.PhotoImage(Image.open("DSP_leer.png"))
#l_grafik = Label(i_fenster, image=s_grafik)
#l_grafik.place(x=530, y=50)

p1 = tk.StringVar()
cb_server_name = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p1)
sql_anweisung = """SELECT DISTINCT server_name FROM ki_energie_importmesswerte
                   ORDER BY server_name"""
a_server_name = db_select(sql_anweisung, None, "ki_energie_importmesswerte")
cb_server_name['values'] = a_server_name
cb_server_name.place(x=250, y=90)
if len(a_server_name) == 1:
    cb_server_name.current(0)

p2 = tk.StringVar()
cb_etage = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p2)
sql_anweisung = """SELECT DISTINCT etage FROM ki_energie_importmesswerte
                   ORDER BY etage"""
a_etage = db_select(sql_anweisung, None, "ki_energie_importmesswerte")
cb_etage['values'] = a_etage
cb_etage.place(x=250, y=120)
cb_etage.bind("<<ComboboxSelected>>", call_cb_etage)
if len(a_etage) == 1:
    cb_etage.current(0)

p3 = tk.StringVar()
cb_raum = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p3)
sql_anweisung = """SELECT DISTINCT raum FROM ki_energie_importmesswerte
                   ORDER BY raum"""
a_raum = db_select(sql_anweisung, None, "ki_energie_importmesswerte")
cb_raum['values'] = a_raum
cb_raum.place(x=250, y=150)
if len(a_raum) == 1:
    cb_raum.current(0)

p4 = tk.StringVar()
cb_sensorklasse = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p4)
sql_anweisung = """SELECT DISTINCT sensorklasse FROM ki_energie_importmesswerte
                   ORDER BY sensorklasse"""
a_sensorklasse = db_select(sql_anweisung, None, "ki_energie_importmesswerte")
cb_sensorklasse['values'] = a_sensorklasse
cb_sensorklasse.place(x=250, y=180)
if len(a_sensorklasse) == 1:
    cb_sensorklasse.current(0)

p5 = tk.StringVar()
cb_name_des_wertes = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p5)
sql_anweisung = """SELECT DISTINCT name_des_wertes FROM ki_energie_importmesswerte
                   ORDER BY name_des_wertes"""
a_name_des_wertes = db_select(sql_anweisung, None, "ki_energie_importmesswerte")
cb_name_des_wertes['values'] = a_name_des_wertes
cb_name_des_wertes.place(x=250, y=210)
if len(a_name_des_wertes) == 1:
    cb_name_des_wertes.current(0)

sql_anweisung = """SELECT DISTINCT DATE_FORMAT(log_datum_vom, '%Y-%m-%d') AS datum FROM ki_energie_importmesswerte
                   GROUP BY datum 
                   ORDER BY datum"""
a_zeitraum = db_select(sql_anweisung, None, "ki_energie_importmesswerte")

p6 = tk.StringVar()
cb_zeitreaum_von = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p6)
cb_zeitreaum_von['values'] = a_zeitraum
cb_zeitreaum_von.place(x=250, y=310)
if len(a_zeitraum) == 1:
    cb_zeitreaum_von.current(0)

p7 = tk.StringVar()
cb_zeitraum_bis = ttk.Combobox(i_fenster, width=20, height=25, textvariable=p7)
cb_zeitraum_bis['values'] = a_zeitraum
cb_zeitraum_bis.place(x=250, y=350)
if len(a_zeitraum) == 1:
    cb_zeitraum_bis.current(0)

ok_button = Button(i_fenster, text="Auswertungsgrafik erzeugen", command=button_action).place(x=20, y=420)
quit_button = Button(i_fenster, text="Beenden", command=i_fenster.destroy).place(x=370, y=420)

i_fenster.mainloop()
