from django.shortcuts import render
from django.http import HttpResponse

# Para acceder a los objetos de la BD
from app_restaurantes.models import Restaurante

# Create your views here.

def index(request):

	# obtener los restaurantes
	restaurantes = Restaurante.objects.all()

	context = {'nuevos_restaurantes':restaurantes[0:4], 'otros_restaurantes':restaurantes[4:15]}
	return render(request, "base.html", context)

def verRestaurante(request, rid):

	# obtener los restaurantes
	restaurante = Restaurante.objects.get(id=rid)
	# obtener todos los restaurantes
	restaurantes = Restaurante.objects.all()
	
	context = {'restaurante':restaurante, 'nuevos_restaurantes':restaurantes[0:4], 'otros_restaurantes':restaurantes[4:15]}

	return render(request, "app_restaurantes/restaurante.html", context)


def login(request):

	context = {'usuario':request.POST.get('email')}
	return render(request, "app_restaurantes/welcome.html", context)


def helloworld(request):

	return HttpResponse("Hello world!")
