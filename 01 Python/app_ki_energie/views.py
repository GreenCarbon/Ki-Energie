from django.shortcuts import render
from django.http import HttpResponse
import datetime
import matplotlib.pyplot as plt


#TEMPLATE_DIRS = (
#    'os.pathsjoin(BASE_DIR, "templates"),'    
#)

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "index.html", {"today": today})

def imp_rpi(request):
    return render(request, "imp_rpi.html")
