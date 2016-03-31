from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Para acceder a los objetos de la BD
from app_restaurantes.models import Restaurante, Plato

# Para usar los formularios
from app_restaurantes.forms import RestauranteForm, PlatoForm

from django.template.defaultfilters import slugify

# Create your views here.

def index(request):

	# obtener los restaurantes
	restaurantes = Restaurante.objects.all()

	num_restaurantes = len(restaurantes)
	inicial = 4

	primeros = num_restaurantes-inicial
	segundos = num_restaurantes-inicial-5

	# platos
	platos = Plato.objects #(tags='mongodb').count()

	context = {'platos':platos, 'nuevos_restaurantes':restaurantes[primeros:num_restaurantes], 'otros_restaurantes':restaurantes[segundos:primeros]}
	return render(request, "base.html", context)

def verRestaurante(request, rid):

	# obtener los restaurantes
	restaurante = Restaurante.objects.get(id=rid)
	# obtener todos los restaurantes
	restaurantes = Restaurante.objects.all()
	
	num_restaurantes = len(restaurantes)
	inicial = 4

	primeros = num_restaurantes-inicial
	segundos = num_restaurantes-inicial-5

	context = {'restaurante':restaurante, 'nuevos_restaurantes':restaurantes[primeros:num_restaurantes], 'otros_restaurantes':restaurantes[segundos:primeros]}

	return render(request, "app_restaurantes/restaurante.html", context)


def verPlato(request, slug):

	plato = Plato.objects(slug=slug)
	if plato:
		plato = plato[0]

	# obtener todos los restaurantes
	restaurantes = Restaurante.objects.all()
	
	num_restaurantes = len(restaurantes)
	inicial = 4

	primeros = num_restaurantes-inicial
	segundos = num_restaurantes-inicial-5

	if plato.megusta != None:
		megustas = len(plato.megusta)
	else:
		megustas = 0
	context = {'plato':plato, 'plato_img': plato.foto.read().encode("base64"), 'megustacount':megustas, 'nuevos_restaurantes':restaurantes[primeros:num_restaurantes], 'otros_restaurantes':restaurantes[segundos:primeros]}

	return render(request, "app_restaurantes/plato.html", context)


def addPlato(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PlatoForm(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL (restaurant info):
			# obtenemos los datos que nos envian
			nombre = form.cleaned_data["nombre"]
			descripcion = form.cleaned_data["descripcion"]

			#foto = form.files.get('foto')
			foto = form.cleaned_data["file"]
			print "Foto: ", foto.name

			# Creamos y guardamos el plato con los datos
			nuevo_plato = Plato(nombre=nombre, descripcion=descripcion)
			nuevo_plato.foto.put(foto, content_type = 'image/jpeg') # put photo
			nuevo_plato = nuevo_plato.save()
			return HttpResponseRedirect('plato/'+str(slugify(nombre)))

    # if a GET (or any other method) we'll create a blank form
    else:
    	form = PlatoForm()

    return render(request, 'app_restaurantes/add_plato.html', {'form': form})


def meGustaPlato(request, slug):

	plato = Plato.objects(slug=slug)
	if plato:
		plato = plato[0]

	usuario = request.user.username
	is_authenticated = request.user.is_authenticated()
	print is_authenticated
	if is_authenticated and not (usuario in plato.megusta):
		plato.megusta.append(usuario)
		plato = plato.save()
		return HttpResponse("OK")
	else:
		return HttpResponse("FAIL")


def addRestaurante(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RestauranteForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL (restaurant info):
			nuevo_restaurante = form.save()
			return HttpResponseRedirect('restaurante/'+str(nuevo_restaurante.id)+'/'+str(nuevo_restaurante.slug))

    # if a GET (or any other method) we'll create a blank form
    else:
    	form = RestauranteForm()

    return render(request, 'app_restaurantes/add_restaurante.html', {'form': form})


def login(request):

	context = {'usuario':request.POST.get('email')}
	return render(request, "app_restaurantes/welcome.html", context)


def helloworld(request):

	return HttpResponse("Hello world!")
