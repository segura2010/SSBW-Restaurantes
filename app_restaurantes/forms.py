
from django.forms import ModelForm

# Para acceder a los objetos de la BD
from app_restaurantes.models import Restaurante

class RestauranteForm(ModelForm):
	class Meta:
		model = Restaurante
		fields = ['nombre', 'direccion', 'email', 'telefono']

