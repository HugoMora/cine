from django import forms
from .models import Local
from .models import Distrito    
from .models import Servicio


class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['nombre', "ubigeo", "fecha_creacion" ]
        

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre', "direccion", "distrito_id", "fecha_creacion" ]
    

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', "local_id" "fecha_creacion" ]
        