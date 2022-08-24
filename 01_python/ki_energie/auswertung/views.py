#from dataclasses import fields
#from urllib import request
#from tkinter import Entry
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


def auswertung(request):
    if request.POST:
        ddl_sel_server = request.POST.get('ddl_server_dsp')
        ddl_sel_etage = request.POST.get('ddl_etagen_dsp')
        ddl_sel_raum = request.POST.get('ddl_raeume_dsp')
        ddl_sel_sensorklasse = request.POST.get('ddl_sensorenklassen_dsp')
        ddl_sel_wert = request.POST.get('ddl_wert_dsp')
        ddl_sel_datum_von = request.POST.get('ddl_datum_von_dsp')
        ddl_sel_datum_bis = request.POST.get('ddl_datum_bis_dsp')
        print('ich bin zurück, hier die Werte: ' + str(ddl_sel_server) + ' '
                                                 + str(ddl_sel_etage) + ' '
                                                 + str(ddl_sel_raum) + ' '
                                                 + str(ddl_sel_sensorklasse) + ' '
                                                 + str(ddl_sel_wert) + ' '
                                                 + str(ddl_sel_datum_von) + ' '
                                                 + str(ddl_sel_datum_bis)
              )

    ddl_server_erg = Raumliste.objects.values(
        'server_name', 'id').order_by('server_name').distinct()
    ddl_etagen_erg = Raumliste.objects.values(
        'etage', 'id').order_by('etage').distinct()
    ddl_raeume_erg = Raumliste.objects.values(
        'raum', 'id').order_by('raum').distinct()
    ddl_sensorklassen_erg = Raumliste.objects.values(
        'raum', 'id').order_by('raum').distinct()
    ddl_wert_erg = Raumliste.objects.values(
        'raum', 'id').order_by('raum').distinct()
    ddl_datum_von_erg = Raumliste.objects.values(
        'raum', 'id').order_by('raum').distinct()
    ddl_datum_bis_erg = Raumliste.objects.values(
        'raum', 'id').order_by('raum').distinct()
    return render(request, "auswertung/auswertung.html", {'ddl_server_erg': ddl_server_erg,
                                                          'ddl_etagen_erg': ddl_etagen_erg,
                                                          'ddl_raeume_erg': ddl_raeume_erg,
                                                          'ddl_sensorklassen_erg': ddl_sensorklassen_erg,
                                                          'ddl_wert_erg': ddl_wert_erg,
                                                          'ddl_datum_von_erg': ddl_datum_von_erg,
                                                          'ddl_datum_bis_erg': ddl_datum_bis_erg
                                                          })
