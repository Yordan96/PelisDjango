from django import forms

from .models import Pelicula, Usuario

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
