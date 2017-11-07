from django.conf.urls import include, url
from . import views
from rentar.views import RegistroUsuario
urlpatterns = [
    url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^alquiler/lista_peliculas/$',  views.lista_peliculas, name ='lista_peliculas'),
    url(r'^alquiler/lista_rentas/$',  views.lista_rentas, name ='lista_rentas'),
    url(r'^alquiler/nueva/$', views.nueva_renta, name='nueva_renta'),
    url(r'^pelicula/nueva/$', views.nueva_pelicula, name='nueva_pelicula'),
    url(r'^pelicula/(?P<pk>[0-9]+)/edit/$', views.editar_pelicula, name='editar_pelicula'),

    url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
    ]
