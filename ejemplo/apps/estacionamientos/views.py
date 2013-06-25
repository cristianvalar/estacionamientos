from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from ejemplo.apps.estacionamientos.models import Estacionamiento, EstacionamientoItem, Ocupacion
from ejemplo.apps.estacionamientos.forms import EstacionamientoForm

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

def nuevoEstacionamiento(request):
	if request.method == "POST":
		formulario = EstacionamientoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/estacionamientos/")
	else:
		formulario = EstacionamientoForm()
		parametros = {"formulario": formulario}
		return render_to_response("nuevoEstacionamiento.html", parametros, context_instance=RequestContext(request))