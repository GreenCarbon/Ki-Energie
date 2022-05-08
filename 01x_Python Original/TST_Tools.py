
import mysql.connector
from CTL_Aktor_Sensor import *
import os
from datetime import *
import logging 
# Für Django hinzugefügt


from django.db import models
import sys 
import os
import django
from ki_energie import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ki_energie.settings')
django.setup()
#from ki_energie.wsgi import *
from ki_energie.models import *





from django.core.asgi import get_asgi_application
from ki_energie.wsgi import *

# Import Anweisungen für interne Klassen & Files
from INT_Classes import *
# Import Anweisungen für interne Klassen & Files
from SQL_Tools import *

SystemInit()
logger = initLogger('root')
con = db_conn()

field_name = 'name'
obj = KiRgActor.objects.first()
field_object = KiRgActor._meta.get_field(field_name)
ActorName = KiRgActor.objects.filter(isactive = 1).filter(id= 1)
field_value = getattr(obj, field_object.attname)
path = os.path.curdir
path2 = os.path.abspath("config.ini")
path3 = os.path.abspath(".")
try:
    aktor_id = 1
    sql_anweisung = """SELECT * FROM ki_rg_actor_sensor 
        WHERE isActive = true and aktor_id="""  + str(aktor_id)
   
    cursor = con.cursor()
    cursor.execute(sql_anweisung)
    sql_erg = cursor.fetchall()
    cursor.close()
           
            
except mysql.connector.Error as error:
        print("Fehler aufgetreten:" + format(error))      
        
         