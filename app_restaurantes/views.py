from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

	context = {'visitor':'visitor'}
	return render(request, "base.html", context)

def login(request):

	context = {'usuario':request.POST.get('email')}
	return render(request, "app_restaurantes/welcome.html", context)


def helloworld(request):

	return HttpResponse("Hello world!")
