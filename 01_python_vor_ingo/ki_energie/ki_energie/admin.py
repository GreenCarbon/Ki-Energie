from django.contrib import admin

from .models import Adressen

# Register your models here.
from ki_energie.models import *

admin.site.register(Adressen)
