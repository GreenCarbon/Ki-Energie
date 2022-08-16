from dataclasses import fields
from urllib import request
from django.shortcuts import render
#from django.http import HttpResponse
#import datetime
#import matplotlib.pyplot as plt
#from django.urls import reverse_lazy
#from django import forms
#from django.views.generic import ListView

#from ki_energie.models import ImportboxFehlerlog
#from ki_energie.models import ImportMesswerte

from .forms import InputForm


def startseite(request):
    return render(request, "auswertung/startseite.html")

def importwerte(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "auswertung/importwerte.html", context)

#class startseite(ListView):
#    model = ImportboxFehlerlog
#    template_name = 'auswertung/startseite.html'


#class import_from_rpi(ListView):
    #model = ImportMesswerte
#    template_name = 'auswertung/import_from_rpi.html'
    #fields = '__all__'
#    context = {}
#    context['form'] = ContactForm()
    #return render(request, "import_from_rpi.html", context)


#TEMPLATE_DIRS = (
#    'os.pathsjoin(BASE_DIR, "templates"),'
#)

#def index(request):
#    today = datetime.datetime.now().date()
#    return render(request, "index.html", {"today": today})

#def imp_rpi(request):
#    return render(request, "imp_rpi.html")
