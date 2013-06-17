from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from ejemplo.apps.estacionamientos.models import Estacionamiento, EstacionamientoItem, Ocupacion

def inicio(request):
	contenido = "<html><body><h1>Hola mundo</h1><p>Saludos desde la UDA</p></body></html>"
	return HttpResponse(contenido)

# def nombre(request, nombre):
# 	# contenido = "<html><body><h1>Hola mundo</h1><p>Mi nombre es %s</p></body></html>" % nombre
# 	parametros = {"usuario": nombre, "apellido": "Valdivia"}
# 	return render_to_response('base.html', parametros)

def estacionamientos(request):
	estacionamientos = Estacionamiento.objects.all()
	parametros = {"estacionamientos": estacionamientos}
	return render_to_response('estacionamientos.html', parametros)

def disponibilidad(request, id_estacionamiento):
	e = get_object_or_404(Estacionamiento, pk=id_estacionamiento)
	estacionamiento_item = EstacionamientoItem.objects.filter(estacionamiento=e, disponible=True)
	cantidad = estacionamiento_item.count()
	parametros = {'estacionamiento': e, 'cantidad': cantidad, 'items': estacionamiento_item}
	return render_to_response('estacionamiento.html', parametros)