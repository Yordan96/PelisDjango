from django.shortcuts import render
from django.contrib import messages
from .forms import UsuarioForm, PeliculaForm
from rentar.models import Pelicula, Alquiler,Usuario
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from rentar.forms import RegistroForm
# Create your views here.

def nueva_renta(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = Usuario.objects.create(nombre=formulario.cleaned_data['nombre'], telefono = formulario.cleaned_data['telefono'], DPI = formulario.cleaned_data['DPI'], fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento'])
            for pelicula_id in request.POST.getlist('peliculas'):
                renta = Alquiler(pelicula_id=pelicula_id, usuario_id = usuario.id)
                renta.save()
            messages.add_message(request, messages.SUCCESS, 'Alquiler Guardada Exitosamente')
            return redirect('lista_peliculas')
    else:
        formulario = UsuarioForm()
    return render(request, 'rentar/alquilar_editar.html', {'formulario': formulario})


def lista_peliculas(request):
    pelis = Pelicula.objects.all()
    return render(request,'rentar/lista_peliculas.html',{'pelis': pelis})

def lista_rentas(request):
    rentas = Alquiler.objects.all()
    return render(request,'rentar/lista_alquileres.html',{'rentas': rentas})

@login_required

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

class RegistroUsuario(CreateView):
    model=User
    template_name= "registration/registrar.html"
    form_class= RegistroForm
    success_url=reverse_lazy('login')

@login_required
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            pelicula = form.save(commit=False)
            pelicula.save()
            return redirect('alquiler/lista_peliculas/')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request,'rentar/pelicula_editar.html',{'form': form})
