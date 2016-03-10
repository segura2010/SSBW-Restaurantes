from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Restaurante (models.Model):
	nombre 		= models.CharField(max_length=30)
	direccion 	= models.CharField(max_length=60)
	email     	= models.EmailField()
	telefono  	= models.CharField(max_length=11)
	slug		= models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Restaurante, self).save(*args, **kwargs)