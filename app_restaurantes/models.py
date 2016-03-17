from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# DB Mongo
from mongoengine import *
connect('restaurantes')

# Create your models here.

class Restaurante(models.Model):
	nombre 		= models.CharField(max_length=30)
	direccion 	= models.CharField(max_length=60)
	email     	= models.EmailField()
	telefono  	= models.CharField(max_length=11)
	slug		= models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Restaurante, self).save(*args, **kwargs)


class Plato(Document):
	nombre 		= StringField(max_length=30)
	descripcion	= StringField(max_length=300)
	comentarios	= ListField(StringField(max_length=140))
	slug 		= StringField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Plato, self).save(*args, **kwargs)