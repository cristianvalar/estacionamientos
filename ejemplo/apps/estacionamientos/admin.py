from django.contrib import admin
from ejemplo.apps.estacionamientos.models import Estacionamiento, EstacionamientoItem, Ocupacion

admin.site.register(Estacionamiento)
admin.site.register(EstacionamientoItem)
admin.site.register(Ocupacion)