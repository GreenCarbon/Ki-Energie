from django.contrib import admin

# Register your models here.
from ki_energie.models import *

#from .models import *

admin.site.register(AuwStatkurven)
admin.site.register(Geraete)
admin.site.register(Geraete2Kunde)
admin.site.register(ImportMesswerte)
admin.site.register(ImportboxFehlerlog)
admin.site.register(KiParams)
admin.site.register(KiRgActor)
