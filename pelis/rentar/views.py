from django.shortcuts import render
from django.contrib import messages
from .forms import UsuarioForm, PeliculaForm
from rentar.models import Pelicula, Alquiler
# Create your views here.

def nueva_renta(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = Usuario.objects.create(nombre=formulario.cleaned_data['nombre'], telefono = formulario.cleaned_data['telefono'], DPI = formulario.cleaned_data['DPI'], fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento'])
            for pelicula_id in request.POST.getlist('peliculas'):
                renta = Alquiler(usuario_id=usuario_id, pelicula_id = pelicula.id)
                renta.save()
            messages.add_message(request, messages.SUCCESS, 'Alquiler Guardada Exitosamente')
    else:
        formulario = UsuarioForm()
    return render(request, 'rentar/alquilar_editar.html', {'formulario': formulario})


def lista_peliculas(request):
    pelis = Pelicula.objects.all()
    return render(request,'rentar/lista_peliculas.html',{'pelis': pelis})

def nueva_pelicula(request):
    if request.method == "POST":
        form =  PeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.save(commit=False)
            pelicula.save()
            return redirect('alquiler/lista_peliculas/')
    else:
        form=PeliculaForm()
    return render(request,'rentar/pelicula_editar.html',{'form': form})
