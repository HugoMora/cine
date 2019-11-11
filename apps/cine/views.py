from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Cliente, Reserva
from .forms import ClienteForm
from .forms import ReservaForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def reservas_index(request):
    return render(request, 'reservas/reservas.html')

def clientes_index(request):
    return render(request, 'clientes/clientes.html')


class Home(TemplateView):
   template_name = 'index.html'

class ListarClientes(ListView):
    model = Cliente
    template_name = 'clientes/listar_cliente.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'

class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/crear_cliente.html'
    success_url = reverse_lazy('cine:listar_clientes')

class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = ''
    success_url = reverse_lazy('')


class EliminarCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = ''
    success_url = reverse_lazy('')

    def get_context_data(self, *args, **kwargs):
        cliente = Cliente.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarCliente, self).get_context_data(*args, **kwargs)
        context['cliente'] = cliente
        return context

# View Reserva

class ListarReservas(ListView):
    model = Reserva
    template_name = 'reservas/listar_reservas.html'
    queryset = Reserva.objects.all()
    context_object_name = 'reserva'

class CrearReserva(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/crear_reserva.html'
    success_url = reverse_lazy('cine:crear_reserva')

class EditarReserva(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = ''
    success_url = reverse_lazy('')


class EliminarReserva(DeleteView):
    model = Reserva
    form_class = ReservaForm
    template_name = ''
    success_url = reverse_lazy('')

    def get_context_data(self, *args, **kwargs):
        reserva = Reserva.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarReserva, self).get_context_data(*args, **kwargs)
        context['reserva'] = reserva
        return context


