
from django import forms
from .models import Cliente
from .models import Reserva
from .models import Distrito
from .models import Actor
from .models import Local
from .models import Servicio
from .models import Categoria
from .models import Genero
from .models import Horario
from .models import Pelicula
from .models import Sala

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'dni']
        labels = {
            'nombre': 'Nombre del Cliente',
            'apellidos': 'Apellidos del Cliente',
            'dni': 'Dni del Cliente'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre del Cliente',
                    'id': 'nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa los apellidos del Cliente',
                    'id': 'apellidos'
                }
            ),
            'dni': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la dni del Cliente',
                    'id': 'dni'
                }
            )
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente_id','pelicula_id', 'fecha', 'cantidad', 'sala_id']
        labels = {
            'cliente_id': 'Nombre del Cliente',
            'pelicula_id': 'Nombre de la Película',
            'fecha': 'Fecha de la Función',
            'cantidad': 'cantidad de asientos',
            'sala_id': 'Sala'
        }
        widgets = {
            'idcliente' : forms.Select(attrs={'class':'form-control'}),
            'idpelicula' : forms.Select(attrs={'class':'form-control'}),
            'fecha' : forms.DateTimeInput(attrs={'class':'form-control'}),
            'cantidad' : forms.TextInput(attrs={'class':'form-control'}),
            'sala_id' : forms.Select(attrs={'class':'form-control'})
        }

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['nombre', 'ubigeo', 'fecha_creacion']
        labels = {
            'nombre': 'Distrito',
            'ubigeo': 'Ubigeo',
            'fecha_creacion': 'Fecha'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'ubigeo' : forms.TextInput(attrs={'class':'form-control'})
            'fecha_creacion' : forms.DateTimeInput(attrs={'class':'form-control'})
        }

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre', 'direccion', 'distrito_id', 'fecha_creacion']
        labels = {
            'nombre': 'Local',
            'direccion': 'Dirección',
            'distrito_id': 'Distrito',
            'fecha_creacion': 'Fecha'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'distrito_id' : forms.Select(attrs={'class':'form-control'}),
            'fecha_creacion' : forms.TextInput(attrs={'class':'form-control'})
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['nombre', 'local_id', 'fecha_creacion']
        labels = {
            'nombre': 'Servicio',
            'local_id': 'Local',
            'fecha_creacion': 'Fecha'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'local_id' : forms.Select(attrs={'class':'form-control'}),
            'fecha_creacion' : forms.DateTimeInput(attrs={'class':'form-control'})
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        labels = {
            'nombre': 'Categoria'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'})
        }
    
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        labels = {
            'nombre': 'Género'
        }  
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'})
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'dni']
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'dni': 'DNI'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'dni' : forms.TextInput(attrs={'class':'form-control'})
        }

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombre', 'apellidos', 'dni']
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'dni': 'DNI',
            'avatar': 'Avatar'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'dni' : forms.TextInput(attrs={'class':'form-control'}),
            'avatar' : forms.ImageInput(attrs={'class':'form-control'})
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['descripcion', 'inicio', 'fin']
        labels = {
            'descripcion': 'Descripción',
            'inicio': 'Inicio',
            'fin': 'Fin'
        }
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'inicio' : forms.TextInput(attrs={'class':'form-control'}),
            'fin' : forms.TextInput(attrs={'class':'form-control'})
        }

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['titulo', 'trailer', 'genero', 'categoria', 'actor', 
            'duracion', 'descripcion', 'imagen', 'idioma', 'fecha_creacion']
        labels = {
            'titulo': 'Título',
            'trailer': 'Trailer',
            'genero': 'Gérnero',
            'categoria': 'Categoría',
            'actor': 'Actor', 
            'duracion': 'Duración',
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
            'idioma': 'Idioma',
            'fecha_creacion': 'Fecha'
        }
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'trailer' : forms.TextInput(attrs={'class':'form-control'}),
            'genero' : forms.Select(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'actor' : forms.Select(attrs={'class':'form-control'}),
            'duracion' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.ImageInput(attrs={'class':'form-control'}),
            'idioma' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_creacion' : forms.DateTimeInput(attrs={'class':'form-control'})
        }

class SalaForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['nombre', 'capacidad', 'horario_id', 'local_id']
        labels = {
            'nombre': 'Sala',
            'capacidad': 'Capacidad',
            'horario_id': 'Horario',
            'local_id': 'Local ID'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'capacidad' : forms.TextInput(attrs={'class':'form-control'}),
            'horario' : forms.Select(attrs={'class':'form-control'}),
            'local_id' : forms.Select(attrs={'class':'form-control'})
        }


