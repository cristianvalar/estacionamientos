#encoding:utf-8

from django.db import models

class Estacionamiento(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=250)
	capacidad_maxima = models.IntegerField(help_text='Capacidad máxima de autos que soporta el Estacionamiento')
	latitud = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
	longitud = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
	fono = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return self.nombre

class EstacionamientoItem(models.Model):
	codigo = models.CharField(max_length=20)
	disponible = models.BooleanField(default=True)
	estacionamiento = models.ForeignKey(Estacionamiento)

	def __unicode__(self):
		return self.codigo

	class Meta:
		verbose_name_plural = "Espacio"

class Ocupacion(models.Model):
	patente = models.CharField(max_length=8)
	entrada = models.DateTimeField()
	salida = models.DateTimeField(null=True, blank=True)
	estacionamientoItem = models.ForeignKey(EstacionamientoItem)

	def __unicode__(self):
		return "%s (%s)" % (self.patente, str(self.entrada))

	class Meta:
		verbose_name_plural = "Ocupación"