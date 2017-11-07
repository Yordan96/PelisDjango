# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=30)),
                ('idioma', models.CharField(max_length=15)),
                ('genero', models.CharField(max_length=15)),
                ('duracion', models.CharField(max_length=15)),
                ('anio', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('DPI', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('peliculas', models.ManyToManyField(through='rentar.Alquiler', to='rentar.Pelicula')),
            ],
        ),
        migrations.AddField(
            model_name='alquiler',
            name='actor',
            field=models.ForeignKey(to='rentar.Usuario'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='pelicula',
            field=models.ForeignKey(to='rentar.Pelicula'),
        ),
    ]
