

from django.conf.urls import patterns, url
from app_restaurantes import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^ng-test/$', TemplateView.as_view(template_name='ng_test.html')), # angular test
	url(r'^index', views.index, name='index'),
	url(r'^restaurante/([0-9]+)/.*', views.verRestaurante, name='verRestaurante'),
	url(r'^addrestaurante', views.addRestaurante, name='addRestaurante'),
	url(r'^plato/(.*)', views.verPlato, name='verPlato'),
	url(r'^addplato', views.addPlato, name='addPlato'),
	url(r'^megustaplato/(.*)', views.meGustaPlato, name='meGustaPlato'),
	url(r'^login', views.login, name='login'),
	url(r'^hello', views.helloworld, name='helloworld'),
	url(r'^api/restaurantes$', views.api_restaurantes, name='api_restaurantes'),
	url(r'^api/restaurante/([\w\-]+)/', views.api_restaurante, name='api_restaurante'),
	url(r'^api/platos$', views.api_platos, name='api_platos'),
	url(r'^api/plato/([\w\-]+)/', views.api_plato, name='api_plato'),
)

