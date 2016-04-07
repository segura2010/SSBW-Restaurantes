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


## RESTAURANTES
# Serializers define the API representation.
class RestauranteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('nombre', 'direccion', 'email', 'telefono', 'slug')



## PLATOS (Mongo: http://stackoverflow.com/questions/17221598/getting-mongoengine-and-django-rest-framework-to-play-nice)
'''

class PlatoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    descripcion = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            for k, v in attrs.iteritems():
                setattr(instance, k, v)
            return instance
        return Plato(**attrs)

'''