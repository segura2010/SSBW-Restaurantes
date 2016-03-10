from django.shortcuts import render
from django.http import HttpResponse

# Para acceder a los objetos de la BD
from app_restaurantes.models import Restaurante

# Create your views here.

def index(request):

	# obtener los restaurantes
	restaurantes = Restaurante.objects.all()[0:4]

	context = {'restaurantes':restaurantes}
	return render(request, "base.html", context)

def login(request):

	context = {'usuario':request.POST.get('email')}
	return render(request, "app_restaurantes/welcome.html", context)


def helloworld(request):

	return HttpResponse("Hello world!")
