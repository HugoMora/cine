from django.shortcuts import render


from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from .forms import CompraForm
from .models import Compra

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'entradas/index.html')

def compra_index(request):
    return render(request, 'entradas/compras.html')



############################################
# CREAR COMPRA #############################
############################################

@require_http_methods(["POST", "GET"])
def crear_compra(request):
    if request.method == 'POST':
        compra_form = LibroForm(request.POST)
        if compra_form.is_valid():
            compra_form.save()
            return redirect('index')
    else:
        compra_form = CompraForm()

    return render(request, 'libro/crear_libro.html', {
        'compra_form': compra_form
    })

#################################
#LISTAR ########################
#################################


@require_http_methods(['GET'])
def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'entradas/listar_compras.html', {
        'compras': compras
    })

  
