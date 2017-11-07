from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^alquiler/lista_peliculas/$',  views.lista_peliculas, name ='lista_peliculas'),
    url(r'^alquiler/nueva/$', views.nueva_renta, name='nueva_renta'),
    url(r'^pelicula/nueva/$', views.nueva_pelicula, name='nueva_pelicula'),
    ]
