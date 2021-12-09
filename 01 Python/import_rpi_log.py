#from getpass import getpass
import mysql.connector
import os
from glob import glob
from datetime import datetime

# --- Routine verarbeitet die einzelnen Zeilen
# --- 1. Inhalt prüfen und bei Fehler ins fehler_log schreiben
# --- 2. positiv geprüften Inhalt in die Tabelle importbox schreiben
def insert_log_zeile(zeile, p_datei, p_satznummer, anzahl_fehler):

    kein_fehler_gefunden = True

    zeile_ary = []
    zeile_ary = zeile.split('|')
    l_log_satzart = zeile_ary[1]

    if l_log_satzart == 'MESSWERT':
        kein_fehler_gefunden = insert_log_zeile_messwert(zeile, p_datei, p_satznummer, anzahl_fehler)
    elif l_log_satzart == 'CONFIG':
        kein_fehler_gefunden = insert_log_zeile_config(zeile, p_datei, p_satznummer, anzahl_fehler)
    else:
        kein_fehler_gefunden = False

    return kein_fehler_gefunden


# --- Routine erzeugt eine Zeile mit Messwerten in Tabelle import_messwerte
def insert_log_zeile_messwert(zeile, p_datei, p_satznummer, anzahl_fehler):

    zeile_ary = []
    zeile_ary = zeile.split('|')
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
            db_verbindung.commit()
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
            fehlertext = 'Der Wert muss einen dezimalen Wert enthalten. Prüf das mal, aber schnell...'
            sql_anweisung = """INSERT INTO importbox_fehlerlog (server_name, datei, fehlertext, satznummer, datensatz) 
                               VALUES(%s, %s, %s, %s, %s)"""
            sql_werte = (p_server_name, p_datei, fehlertext,
                         p_satznummer, zeile)

            db_ergebnis = cursor.execute(sql_anweisung, sql_werte)
            db_verbindung.commit()

        except mysql.connector.Error as error:
            print("Fehler beim Schreiben in die importbox_fehlerlog: {}".format(error))
            kein_fehler_gefunden = False

    return kein_fehler_gefunden


def insert_log_zeile_config(zeile, p_datei, p_satznummer):
    
    kein_fehler_gefunden = True
    
    zeile_ary = []
    zeile_ary = zeile.split('|')
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


# --- Archivierungsroutine ---
def archiv_logdatei(p_log_pfad, p_log_extension, p_log_verarbeitet):
    if p_log_verarbeitet:
        for filenames in glob(p_log_pfad + p_log_extension):
            datei = filenames.replace(p_log_pfad, "")
            datei_archiv = p_log_pfad + "Archiv/" + aktuelle_zeit + '_' + datei
            os.rename(filenames, datei_archiv)


# --- Beginn des Hauptprogramms ---

aktuelle_zeit = datetime.now().strftime('%Y%m%d-%H%M%S')  
                            # Format = 20211109-131856
log_pfad = os.getenv('HOME') + '/Entwicklung/LogFiles/'
log_datei = 'devlog*'
satznummer = 0
anzahl_dateien = 0
anzahl_saetze = 0
anzahl_fehler = 0
v_dateiname = None 

os.chdir(log_pfad)
log_dateien = sorted(glob(log_datei), key=os.path.basename)

db_verbindung = mysql.connector.connect(database='DeCarbonara',
                                            user='root',
                                        password='DeCarbonaras#2021') 
                                        #password=getpass("Enter password: "))
                                        
cursor = db_verbindung.cursor()


for dateien in log_dateien:
    datei = open(f'{dateien}', 'r')
    # - mit dem Beginn einer neuen Datei wird der Satzzähler auf 0 zurückgesetzt
    if v_dateiname is not datei.name:
        v_dateiname = datei.name
        satznummer = 0
        anzahl_dateien += 1

    for zeile in datei:
        satznummer += 1
        anzahl_saetze += 1
        kein_fehler_gefunden = insert_log_zeile(zeile, datei.name, satznummer, anzahl_fehler)

if db_verbindung.is_connected():
   cursor.close()
   db_verbindung.close()

print('Es wurden ' + str(anzahl_dateien) + ' Dateien verarbeitet und insgesamt ' + str(anzahl_saetze) + ' Datensätze in die Tabelle geschrieben.')
print('Es wurden ' + str(anzahl_fehler) + ' Fehler protokolliert.')

# - noch schnell alle Dateien ins Archiv-Verzeichnis verschieben
archiv_logdatei(log_pfad, log_datei, kein_fehler_gefunden)


