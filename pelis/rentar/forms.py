from django import forms

from .models import Pelicula, Usuario

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UsuarioForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Usuario
        fields = ('nombre', 'telefono', 'DPI', 'fecha_nacimiento', 'peliculas')

    def __init__ (self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields["peliculas"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["peliculas"].help_text = "Seleccióne las peliculas que quiere alquilar"
        self.fields["peliculas"].queryset = Pelicula.objects.all()

class PeliculaForm(forms.ModelForm):
    class Meta:
        model= Pelicula
        fields =('titulo','idioma','genero','duracion','anio')

class RegistroForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email',)
        labels={'username':'Nombre de usuario','firts_name':'nombre','last_name':'apellido','email':'Correo',}
