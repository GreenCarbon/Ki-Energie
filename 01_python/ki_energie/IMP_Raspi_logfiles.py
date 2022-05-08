#from getpass import getpass
import mysql.connector
import os
from glob import glob
from datetime import datetime
from tkinter import *


# Import Anweisungen für interne Klassen & Files
from INT_Classes import *
from SQL_Tools import *

SystemInit()
con = db_conn()

# --- Beginn des Hauptprogramms ---

global aktuelle_zeit
aktuelle_zeit = datetime.now().strftime('%Y%m%d-%H%M%S')  # Format = 20211109-131856

global my_label1
global my_label2

cursor = con.cursor()

root = Tk()
root.geometry("500x500")
root.title('Import LOG-Files')

my_label1 = Label(root, text='')
my_label1.pack(pady=10)

my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

my_listbox = Listbox(my_frame, width=20, height=15, yscrollcommand=my_scrollbar.set, selectmode=EXTENDED)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(pady=10, side=RIGHT, fill=Y)
my_frame.pack()

my_listbox.pack(pady=10)

global log_pfad
#log_pfad = os.getenv('HOME') + '/Decarbonara/Ki-Energie/03 LogFiles/'
log_pfad = getConfigParam("ENVIRONMENT", "datafiles")
#os.chdir(log_pfad)
log_datei = 'devlog*'

label_pfad = 'Ausgewählter Suchpfad für die Log-Dateien: ' + '\n' + log_pfad
my_label1.config(text=label_pfad)

os.chdir(log_pfad)
log_dateien = sorted(glob(log_datei), key=os.path.basename)

for dateien in log_dateien:
    my_listbox.insert(END, dateien)


def select_verarbeiten():
    anzahl_fehler = 0
    result = ''
    kein_fehler_gefunden = True
    __my_selection = []
    
    for item in my_listbox.curselection():
        datei_verarbeitet = str(my_listbox.get(item))
        datei_select = log_pfad + datei_verarbeitet
        #datei = codecs.open(f'{dateien}', 'r', encoding="ascii", errors="surrogateescape")
        # - mit dem Beginn einer neuen Datei wird der Satzzähler auf 0 zurückgesetzt
        datei = open(f'{datei_select}', 'rb')
        satznummer = 0
        
# --- Zeile für Zeile wird hier gelesen, geprüft und in die DB geschrieben
        for zeile in datei:
            satznummer += 1
            zeile_str = zeile.decode('unicode_escape').encode('utf-8')
            insert_log_zeile(zeile_str, datei.name, satznummer, anzahl_fehler)
       
# --- Ausgabe der verarbeiteten Dateien im Fenster
        result = result + 'Datei: ' + datei_verarbeitet + ' gelesen ' + str(satznummer) + ' fehlerhaft ' + str(anzahl_fehler) + '\n' 
        my_label2.config(text=result)

        datei_archiv = log_pfad + "Archiv/" + aktuelle_zeit + '_' + datei_verarbeitet
        os.rename(datei_select, datei_archiv)

        
# --- hier noch schnell die Listbox bereinigen
    __my_selection = my_listbox.curselection()
    for index in reversed(__my_selection):
        my_listbox.delete(index)
    

# --- Routine verarbeitet die einzelnen Zeilen
# --- 1. Inhalt prüfen und bei Fehler ins fehler_log schreiben
# --- 2. positiv geprüften Inhalt in die Tabelle importbox schreiben
def insert_log_zeile(zeile, p_datei, p_satznummer, anzahl_fehler):

    zeile_ary = []
    str_zeile = zeile.decode().replace(';','|')
    zeile_ary = str_zeile.split('|')
    l_log_satzart = zeile_ary[1]

    if l_log_satzart == 'MESSWERT':
        anzahl_fehler = 0
        insert_log_zeile_messwert(zeile, p_datei, p_satznummer, anzahl_fehler)
    elif l_log_satzart == 'CONFIG':
        anzahl_fehler = 0
        insert_log_zeile_config(zeile, p_datei, p_satznummer)


# --- Routine erzeugt eine Zeile mit Messwerten in Tabelle import_messwerte
def insert_log_zeile_messwert(zeile, p_datei, p_satznummer, anzahl_fehler):
    
    zeile_ary = []
    str_zeile = zeile.decode().replace(';','|')
    zeile_ary = str_zeile.split('|')
    if len(zeile_ary) < 10: 
        print("Zeile enthält keine 9 Felder :" , zeile)
        kein_fehler_gefunden = False
        return kein_fehler_gefunden
    
    l_log_datum_vom = zeile_ary[0]
    l_server_name = zeile_ary[2]
    l_etage = zeile_ary[3]
    l_raum = zeile_ary[4]
    l_geraete_name = zeile_ary[5]
    l_name_des_wertes = zeile_ary[6]
    l_wert = zeile_ary[7]
    l_sensorklasse = zeile_ary[8]
    l_name_sensorklasse = zeile_ary[9]

    l_wert_num = None
    l_wert_bit = None
    l_wert_str = l_wert
    if l_wert == 'true':
        l_wert_bit = True
        l_wert_str = None
        kein_fehler_gefunden = True
        satz_kann_geschrieben_werden = True
    elif l_wert == 'false':
        l_wert_bit = False
        l_wert_str = None
        kein_fehler_gefunden = True
        satz_kann_geschrieben_werden = True
    else:
        kein_fehler_gefunden = chk_log_zeile_messwert(zeile, p_datei, p_satznummer, l_server_name, l_wert, anzahl_fehler)
        if kein_fehler_gefunden:
            l_wert_num = l_wert
            l_wert_str = None
            satz_kann_geschrieben_werden = True
        elif not kein_fehler_gefunden:
            anzahl_fehler += 1

    if satz_kann_geschrieben_werden:
        
        try:
            sql_anweisung = """INSERT INTO import_messwerte (log_datum_vom, server_name, etage, raum, geraete_name, 
                                name_des_wertes, wert_num, wert_bit, wert_str, sensorklasse, name_sensorklasse)
                               VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            sql_werte = (l_log_datum_vom, l_server_name, l_etage, l_raum, l_geraete_name,
                         l_name_des_wertes, l_wert_num, l_wert_bit, l_wert_str, l_sensorklasse, l_name_sensorklasse)

            db_ergebnis = cursor.execute(sql_anweisung, sql_werte)
            con.commit()
            #print("Alle Daten wurden fehlerfrei importiert")

        except mysql.connector.Error as error:
            print("Fehler beim Schreiben in die import_messwerte: {}".format(error))
            kein_fehler_gefunden = False
                
    return kein_fehler_gefunden


# --- Routine die eine Zeile auf korrekten Inhalt prüft und bei Fehler ins fehler_log schreibt
def chk_log_zeile_messwert(zeile, p_datei, p_satznummer, p_server_name, p_wert, anzahl_fehler):

    kein_fehler_gefunden = True

    __ist_wert_num = chk_str_is_float(p_wert)

    if not __ist_wert_num:
        anzahl_fehler += 1
        kein_fehler_gefunden = False
        try:
            str_zeile = zeile.decode().replace(';','|')
            fehlertext = 'Der Wert muss einen dezimalen Wert enthalten. Prüf das mal, aber schnell...'
            sql_anweisung = """INSERT INTO importbox_fehlerlog (server_name, datei, fehlertext, satznummer, datensatz) 
                               VALUES(%s, %s, %s, %s, %s)"""
            sql_werte = (p_server_name, p_datei, fehlertext,
                         p_satznummer, str_zeile)

            db_ergebnis = cursor.execute(sql_anweisung, sql_werte)
            con.commit()

        except mysql.connector.Error as error:
            print("Fehler beim Schreiben in die importbox_fehlerlog: {}".format(error))
            kein_fehler_gefunden = False

    return kein_fehler_gefunden


def insert_log_zeile_config(zeile, p_datei, p_satznummer):
    
    kein_fehler_gefunden = True
    
    zeile_ary = []
    str_zeile = zeile.decode().replace(';','|')
    zeile_ary = str_zeile.split('|')
    l_log_datum_vom = zeile_ary[0]
    l_server_name = zeile_ary[2]

    return kein_fehler_gefunden


# --- die kleine Routine prüft den Parameterwert auf gültigen INT oder DECIMAL Wert
def chk_str_is_float(__s):
    try:
        float(__s)
        return True
    except:
        return False

my_select_button = Button(root, text="Selektierte verarbeiten", command=select_verarbeiten)
my_select_button.pack(pady=10)

my_label2 = Label(root, text='')
my_label2.pack(pady=5)

root.mainloop()

if con.is_connected():
   cursor.close()
   con.close()
