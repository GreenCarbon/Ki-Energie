# from dataclasses import fields
# from urllib import request
# from tkinter import Entry
from django.shortcuts import render
# from django.http import HttpResponse
# import datetime
# import matplotlib.pyplot as plt
from datetime import *

from ki_energie.models import Kunde, Raumliste, Etage
from auswertung.ASW_Messwerte import *


def startseite(request):
    return render(request, "auswertung/startseite.html", {})


def importwerte(request):
    rl = Raumliste.objects.all().order_by('log_erzeugt_am')
    return render(request, "auswertung/importwerte.html", {'Erg': rl})


def auswertung(request):

    ddl_sel_kunde = 0
    ddl_sel_server = 0
    ddl_sel_etage = 0
    ddl_sel_raum = 0
    ddl_sel_sensorklasse = 0
    ddl_sel_wert = 0
    ddl_sel_datum_von = 0
    ddl_sel_datum_bis = 0

    ddl_kunde_erg = []
    ddl_server_erg = []
    ddl_etagen_erg = []
    ddl_raeume_erg = []
    ddl_sensorklassen_erg = []
    ddl_wert_erg = []
    ddl_datum_von_erg = []
    ddl_datum_bis_erg = []

    dsp_eckdaten = False
    dsp_auswertung = False

    if request.POST:
        ddl_sel_kunde = request.POST.get('ddl_kunde_dsp')
        if ddl_sel_kunde != 0:
            ddl_server_erg = Raumliste.objects.values(
                'server_name', 'id').order_by('server_name').distinct()
            ddl_etagen_erg = Etage.objects.values(
                'name', 'id').filter(gebaeude_id=1).order_by('name')
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

            ddl_sel_server = request.POST.get('ddl_server_dsp')
            ddl_sel_etage = request.POST.get('ddl_etagen_dsp')
            ddl_sel_raum = request.POST.get('ddl_raeume_dsp')
            ddl_sel_sensorklasse = request.POST.get('ddl_sensorenklassen_dsp')
            ddl_sel_wert = request.POST.get('ddl_wert_dsp')
            ddl_sel_datum_von = request.POST.get('ddl_datum_von_dsp')
            ddl_sel_datum_bis = request.POST.get('ddl_datum_bis_dsp')

            grafiken.graf_erzeugen(ddl_sel_server, ddl_sel_etage, ddl_sel_raum, ddl_sel_sensorklasse,
                                   ddl_sel_wert, ddl_sel_datum_von, ddl_sel_datum_bis)
            dsp_eckdaten = True
            dsp_auswertung = True

    ddl_kunde_erg = Kunde.objects.values(
        'nachname', 'id', 'vorname', 'anrede', 'titel').order_by('nachname').distinct()

    return render(request, "auswertung/auswertung.html", {'ddl_kunde_erg': ddl_kunde_erg,
                                                          'ddl_sel_kunde': ddl_sel_kunde,
                                                          'ddl_server_erg': ddl_server_erg,
                                                          'ddl_etagen_erg': ddl_etagen_erg,
                                                          'ddl_raeume_erg': ddl_raeume_erg,
                                                          'ddl_sensorklassen_erg': ddl_sensorklassen_erg,
                                                          'ddl_wert_erg': ddl_wert_erg,
                                                          'ddl_datum_von_erg': ddl_datum_von_erg,
                                                          'ddl_datum_bis_erg': ddl_datum_bis_erg,
                                                          'dsp_eckdaten': dsp_eckdaten,
                                                          'show_auswertung': dsp_auswertung
                                                          })
