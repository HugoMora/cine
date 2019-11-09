from django import forms
from .models import Cliente, Reserva

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
            'cliente_id': 'Nombre del Cliente'
            'pelicula_id': 'Nombre de la Película',
            'fecha': 'Fecha de la Función',
            'cantidad': 'cantidad de asientos',
            'sala_id': 'Sala'
        }

        widgets = {
            'idcliente' : forms.Select(attrs={'class':'form-control'}),
            'idpelicula' : forms.Select(attrs={'class':'form-control'}),
            'fecha' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad' : forms.TextInput(attrs={'class':'form-control'}),
            'sala_id' : forms.Select(attrs={'class':'form-control'})
        }

