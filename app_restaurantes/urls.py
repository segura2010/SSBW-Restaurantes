

from django.conf.urls import patterns, url
from app_restaurantes import views

urlpatterns = patterns('',
	url(r'^index', views.index, name='index'),
	url(r'^restaurante/([0-9]+)/.*', views.verRestaurante, name='verRestaurante'),
	url(r'^addrestaurante', views.addRestaurante, name='addRestaurante'),
	url(r'^login', views.login, name='login'),
	url(r'^hello', views.helloworld, name='helloworld')
)

