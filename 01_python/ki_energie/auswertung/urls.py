"""django_ki_energie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#from django.conf.urls import url
#from ki_energie import views
#from auswertung import views
from .views import startseite
from .views import importwerte
#from auswertung.views import startseite, importwerte

#app_name = 'auswertung'
urlpatterns = [
   # path('', start.as_view(), name='Startseite'),
    path('', startseite, name='startseite'),
   # url('', startseite, name='startseite'),
   # url('imp/', importwerte, name='importwerte')
    path('imp/', importwerte, name='importwerte')
    #path('', .as_view(), name='Startseite')
]
