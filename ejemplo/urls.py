from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ejemplo.apps.estacionamientos.views.inicio', name='inicio'),
    # url(r'^nombre/(?P<nombre>\w+)$', 'ejemplo.apps.estacionamientos.views.nombre', name='nombre'),
    url(r'^estacionamientos/$', 'ejemplo.apps.estacionamientos.views.estacionamientos', name='estacionamientos'),
    url(r'^estacionamiento/(?P<id_estacionamiento>\d+)$', 'ejemplo.apps.estacionamientos.views.disponibilidad', name='disponibilidad'),

    url(r'^admin/', include(admin.site.urls)),
)