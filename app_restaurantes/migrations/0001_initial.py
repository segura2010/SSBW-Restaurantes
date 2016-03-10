# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=11)),
                ('slug', models.SlugField()),
            ],
        ),
    ]