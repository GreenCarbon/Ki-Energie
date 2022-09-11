# Django Framework
import logging
from configparser import ConfigParser
from ki_energie.models import *
from ki_energie.SQL_Tools import *
from django.db import models
import sys
import os
import django
from datetime import *
import ki_energie.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ki_energie.settings')
django.setup()

#-------------------------------------------------------------
# Handling der Einträge für unsere Kunden
#-------------------------------------------------------------
class KI_Kunde:
    pass

    def __init__(self, id):
        pass

# Aufruf der Systeminitialisierung. Hat alles funktioniert, wird True zurückgeliefert, bei Fehlern FALS
    def new():

        return True

#-------------------------------------------------------------
# Handling der Einträge für KI-Raspi-Server
#-------------------------------------------------------------
class KI_Server:
    """ Class for Server Objects Handling """
    
    def __init__(self, id=0, name = "", srv=Server()) :
        self.id = id
        self.name = name
        self.srv = srv
        
    # Wenn der Server nicht existiert, wird er automatisch angelegt. Die Ergänzung der fehlenden Daten muss später nachgeholt werden    
    def find_by_name(self, name): 
        """ Find the Server buy name """
        # Find the server by name
        try:
            srv = Server.objects.get(name=name)
            id = getattr(srv, "id")
        except Server.DoesNotExist:
            return 0
        return id
    
    # Wenn der Server nicht existiert, wird er automatisch angelegt. Die Ergänzung der fehlenden Daten muss später nachgeholt werden
    def get_or_create_by_name(self, name): 
        """Trying to find the Server, if not exists, the Server will created in Table"""
        try:
            srv = Server.objects.get(name=name)
            id = getattr(srv, "id")
        except Server.DoesNotExist:
            srv1 = Server.objects.order_by('-id').first()
            id = getattr(srv1, "id") + 1
            logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            srv = Server(id=id, name=name, comment="*AUTOMATISCHE ANLAGE!", log_datum_vom=logdat)
            srv.save()
            self.srv = srv
        return id

    def find_by_id(self, id): #Sucht und merkt (wenn gefunden) einen Server per ID
        """Search Server record by ID, return TRUE or FALSE if OK / NOT OK"""
        
        try:
            srv = Server.objects.get(id=id)
            self.srv = srv
        except Server.DoesNotExist:
            return False
        return True


    def create(self, name, kunde):
        """Create a new Server Record, return True if OK, if Not return FALSE"""
        try:
            srv1 = Server.objects.order_by('-id').first()
            id = getattr(srv1, "id") + 1
            logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            srv = Server(id=id, name=name, kunde_id = kunde, comment="*AUTOMATISCHE ANLAGE!", log_datum_vom=logdat)
            srv.save()
            self.srv = srv
        except:
            return False
        return True

    
    def get_name(self, id):
        """Search Server record by ID, return Server name or '' """
        try:
            srv = Server.objects.get(id=id)
            self.srv = srv
            return getattr(srv, "name")
        except Server.DoesNotExist:
            return ''
                


    def get_kunde(self, id):
        """Search Server record by ID, return kunde_id name or 0 """
        try:
            srv = Server.objects.get(id=id)
            self.srv = srv
            return getattr(srv, "kunde_id")
        except Server.DoesNotExist:
            return 0


#-------------------------------------------------------------
# Handling der Einträge für KI-Räume
#-------------------------------------------------------------
class KI_Raum:
    """ Class for Rooms Objects Handling """
    def __init__(self, id=0, name = "", kunde = 0, server = 0, gebaeude = 0, etage =0, raum = Raumliste()) :
        self.id = id
        self.name = name
        self.kunde = kunde
        self.etage = etage
        self.raum = raum
        self.gebaeude = gebaeude
        
        
    # Wenn der Raum nicht existiert, wird er automatisch angelegt. Die Ergänzung der fehlenden Daten muss später nachgeholt werden    
    def find_by_name(self, name, kunde, gebaude, server, etage): 
        try:
            rl = Raumliste.objects.get(name=name, kunde_id = kunde, gebaude_id = gebaude, server_id = server, etage_id = etage)
            id = getattr(rl, "id")
        except Raumliste.DoesNotExist:
            return 0
        return id
    
    # Wenn der Raum nicht existiert, wird er automatisch angelegt. Die Ergänzung der fehlenden Daten muss später nachgeholt werden
    def get_or_create_by_name(self, name, kunde, gebaude, server, etage): 
        """Trying to find the Room, if not exists, the Room will created in Table"""
        try:
            rl = Raumliste.objects.get(name=name, kunde_id = kunde, gebaude_id = gebaude, server_id = server, etage_id = etage )
            id = getattr(rl, "id")
        except Raumliste.DoesNotExist:
            rl1 = Raumliste.objects.order_by('-id').first()
            id = getattr(rl1, "id") + 1
            logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rl1 = Raumliste(id=id, name=name, kunde_id = kunde, gebaude_id = gebaude, server_id = server, etage_id = etage, comment="*AUTOMATISCHE ANLAGE!", log_datum_vom=logdat)
            rl1.save()
            self.raum = rl1
        return id

    def find_by_id(self, id): #Sucht und merkt (wenn gefunden) einen Raum per ID
        """Search Room record by ID, return TRUE or FALSE if OK / NOT OK"""
        
        try:
            rl1 = Raumliste.objects.get(id=id)
            self.raum = rl1
        except Raumliste.DoesNotExist:
            return False
        return True


    def create(self, name, kunde, gebaude, server, etage):
        """Create a new Room Record, return True if OK, if Not return FALSE"""
        try:
            rl1 = Raumliste.objects.order_by('-id').first()
            id = getattr(rl1, "id") + 1
            logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rl1 = Raumliste(id=id, name=name, kunde_id = kunde, gebaude_id = gebaude, server_id = server, etage_id = etage, comment="*AUTOMATISCHE ANLAGE!", log_datum_vom=logdat)
            rl1.save()
            self.raum = rl1
        except:
            return False
        return True

    
    def get_name(self, id):
        """Search Rooms record by ID, return Server name or '' """
        try:
            rl1 = Raumliste.objects.get(id=id)
            self.raum = rl1
            return getattr(rl1, "name")
        except Raumliste.DoesNotExist:
            return ''
                


    def get_kunde(self, id):
        """Search Room record by ID, return kunde_id name or 0 """
        try:
            rl1 = Raumliste.objects.get(id=id)
            self.raum = rl1
            return getattr(rl1, "kunde_id")
        except Server.DoesNotExist:
            return 0

#-------------------------------------------------------------
# Handling der Einträge für KI-Etagen
#-------------------------------------------------------------
class KI_Etage:
    """ Class for Floors Objects Handling """
    def __init__(self, id=0, name = "",  gebaeude = 0, etage = Etage()) :
        self.id = id
        self.name = name
        self.etage = etage
        self.gebaeude = gebaeude
        
        
    # Wenn die Etage nicht existiert, wird er automatisch angelegt. Die Ergänzung der fehlenden Daten muss später nachgeholt werden    
    def find_by_name(self, name, gebaude, server, etage): 
        try:
            el = Etage.objects.get(name=name, gebaude_id = gebaude, )
            id = getattr(el, "id")
        except Etage.DoesNotExist:
            return 0
        return id
    
    # Wenn die Etage nicht existiert, wird sie automatisch angelegt. Die Ergänzung der fehlenden Daten muss später nachgeholt werden
    def get_or_create_by_name(self, name,  gebaude): 
        """Trying to find the Floor, if not exists, the Floor will created in Table"""
        try:
            el = Etage.objects.get(name=name, gebaude_id = gebaude )
            id = getattr(wl, "id")
        except Etage.DoesNotExist:
            el1 = Etage.objects.order_by('-id').first()
            id = getattr(el1, "id") + 1
            logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            el1 = Etage(id=id, name=name, gebaude_id = gebaude,  comment="*AUTOMATISCHE ANLAGE!", log_datum_vom=logdat)
            el1.save()
            self.etage = el1
        return id

    def find_by_id(self, id): #Sucht und merkt (wenn gefunden) eine Etage per ID
        """Search Floors record by ID, return TRUE or FALSE if OK / NOT OK"""
        
        try:
            el1 = Etage.objects.get(id=id)
            self.etage = el1
        except Etage.DoesNotExist:
            return False
        return True


    def create(self, name, gebaude):
        """Create a new Floor Record, return True if OK, if Not return FALSE"""
        try:
            el1 = Etage.objects.order_by('-id').first()
            id = getattr(el1, "id") + 1
            logdat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            el1 = Raumliste(id=id, name=name,  gebaude_id = gebaude, comment="*AUTOMATISCHE ANLAGE!", log_datum_vom=logdat)
            el1.save()
            self.raum = el1
        except:
            return False
        return True

    
    def get_name(self, id):
        """Search Etage record by ID, return Etage name or '' """
        try:
            el1 = Etage.objects.get(id=id)
            self.raum = el1
            return getattr(el1, "name")
        except Etage.DoesNotExist:
            return ''
                


    def get_kunde(self, id):
        """Search Room record by ID, return kunde_id name or 0 """
        try:
            rl1 = Raumliste.objects.get(id=id)
            self.raum = rl1
            return getattr(rl1, "kunde_id")
        except Server.DoesNotExist:
            return 0