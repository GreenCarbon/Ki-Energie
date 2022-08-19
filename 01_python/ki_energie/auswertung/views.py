#from dataclasses import fields
#from urllib import request
from tkinter import Entry
from django.shortcuts import render
#from django.http import HttpResponse
#import datetime
#import matplotlib.pyplot as plt

#from ki_energie.models import ImportboxFehlerlog
#from ki_energie.models import ImportMesswerte
from ki_energie.models import Raumliste

def startseite(request):
    return render(request, "auswertung/startseite.html", {})

def importwerte(request):
    rl = Raumliste.objects.all().order_by('log_erzeugt_am')
    return render(request, "auswertung/importwerte.html", {'Erg': rl})

def raumliste(request):
    ddl_server_erg = Raumliste.objects.values(
        'server_name', 'id').order_by('server_name').distinct()
    ddl_etage_erg = Raumliste.objects.values(
        'etage', 'id').order_by('etage').distinct()
    ddl_raumliste_erg = Raumliste.objects.values(
        'raum', 'id').order_by('raum').distinct()
    return render(request, "auswertung/raumliste.html", {'ddl_server_erg': ddl_server_erg,
                                                         'ddl_etage_erg': ddl_etage_erg,
                                                         'ddl_raumliste_erg': ddl_raumliste_erg})
