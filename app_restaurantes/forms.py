
from django.forms import ModelForm, Form

from django import forms

# Para acceder a los objetos de la BD
from app_restaurantes.models import Restaurante, Plato

class RestauranteForm(ModelForm):
	class Meta:
		model = Restaurante
		fields = ['nombre', 'direccion', 'email', 'telefono']


class PlatoForm(forms.Form):
	nombre = forms.CharField(label='Nombre', max_length=30)
	descripcion = forms.CharField(label='Descripcion', max_length=300)
	file = forms.FileField(label='Foto')
