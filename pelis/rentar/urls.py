from django.conf.urls import include, url
from . import views
from rentar.views import RegistroUsuario
urlpatterns = [
    url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^alquiler/lista_peliculas/$',  views.lista_peliculas, name ='lista_peliculas'),
    url(r'^alquiler/nueva/$', views.nueva_renta, name='nueva_renta'),
    url(r'^pelicula/nueva/$', views.nueva_pelicula, name='nueva_pelicula'),
    url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
    ]
