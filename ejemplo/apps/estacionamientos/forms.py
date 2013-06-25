from django.forms import ModelForm
from ejemplo.apps.estacionamientos.models import Estacionamiento

class EstacionamientoForm(ModelForm):
	class Meta:
		model = Estacionamiento