"""Restaurantes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User

from app_restaurantes.models import Restaurante, Plato

# Rest Framework
from rest_framework import routers, serializers, viewsets, generics

## USERS
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

## RESTAURANTES
# Serializers define the API representation.
class RestauranteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('nombre', 'direccion', 'email', 'telefono', 'slug')

# ViewSets define the view behavior.
class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

'''
## PLATOS (Mongo: http://stackoverflow.com/questions/17221598/getting-mongoengine-and-django-rest-framework-to-play-nice)
# Serializers define the API representation.
class PlatoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    descripcion = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            for k, v in attrs.iteritems():
                setattr(instance, k, v)
            return instance
        return Plato(**attrs)

# ViewSets define the view behavior.
class PlatoViewSet(generics.ListCreateAPIView):
    serializer_class = PlatoSerializer
    def get_queryset(self):
        return Plato.objects
'''

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurantes', RestauranteViewSet)
#router.register(r'platos', PlatoViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^resta/', include('app_restaurantes.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
