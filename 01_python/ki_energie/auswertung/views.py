from dataclasses import fields
from django.shortcuts import render
#from django.http import HttpResponse
#import datetime
#import matplotlib.pyplot as plt
from django.urls import reverse_lazy
from django.views.generic import ListView

from ki_energie.models import ImportboxFehlerlog
from ki_energie.models import ImportMesswerte


class start(ListView):
    model = ImportboxFehlerlog
    template_name = 'start.html'


class import_from_rpi(ListView):
    model = ImportMesswerte
    template_name = 'import_from_rpi.html'
    fields = '__all__'


#TEMPLATE_DIRS = (
#    'os.pathsjoin(BASE_DIR, "templates"),'
#)

#def index(request):
#    today = datetime.datetime.now().date()
#    return render(request, "index.html", {"today": today})

#def imp_rpi(request):
#    return render(request, "imp_rpi.html")
