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
from app_restaurantes import views

from rest_framework import routers, serializers, viewsets, generics

from app_restaurantes.serializers import RestauranteSerializer, UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'restaurantes', views.RestauranteViewSet)
#router.register(r'platos', PlatoViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^resta/', include('app_restaurantes.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
