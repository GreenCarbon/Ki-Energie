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
from .views import startseite, importwerte, auswertung, get_json_kunden_daten

urlpatterns = [
    path('', startseite, name='startseite'),
    path('import/', importwerte, name='importwerte'),
    path('auswertung/', auswertung, name='auswertung'),
    path('kunden-daten/', get_json_kunden_daten, name='kunden-daten'),
    path('server-daten/<str:kunde>', get_json_kunden_daten, name='server-daten')
]
