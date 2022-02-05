# Haupteinstiegspunkt in das Programm

from INT_Classes import *

SystemInit()
logger = initLogger('root')
con = db_conn()

runscript = getConfigParam("APPLICATION", "FUNCTION")
# Ausführen Anzeige der Raumwerte
if (runscript == "GRAFIK"):
    exec(open("/Users/Karsten/Alles/Kunden/Decarbonara/01 Workspace_GIT/01 Python/DSP_RPI_LOG.py").read())
    
if (runscript == "STATISTIK"):
    exec(open("/Users/Karsten/Alles/Kunden/Decarbonara/01 Workspace_GIT/01 Python/AUW_STATS.py").read())

# Ausführen Raumcontroller 
if (runscript == "CONTROLLER"):
    exec(open("/Users/Karsten/Alles/Kunden/Decarbonara/01 Workspace_GIT/01 Python/CTL_RAUM_TEMP.py").read())
    
    