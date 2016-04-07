from django.contrib.auth.models import User

from app_restaurantes.models import Restaurante, Plato

# Rest Framework
from rest_framework import routers, serializers, viewsets, generics

## USERS
# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


## RESTAURANTES
# Serializers define the API representation.
class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('nombre', 'direccion', 'email', 'telefono', 'slug')


class PlatoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    slug = serializers.CharField()
    comentarios = serializers.ListField(serializers.CharField())
    #foto = serializers.CharField()