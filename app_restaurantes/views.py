from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, visitor):

	context = {'visitor':visitor}
	return render(request, "base.html", context)


def helloworld(request):

	return HttpResponse("Hello world!")
