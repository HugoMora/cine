from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import ClienteForm, ReservaForm
from .models import Cliente, Reserva
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class ListarClientes(ListView):
    model = Cliente
    template_name = 'cine/cliente/listar_cliente.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'

class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cine/cliente/crear_cliente.html'
    success_url = reverse_lazy('cine:listar_clientes')

class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cine/cliente/editar_cliente.html'
    success_url = reverse_lazy('cine:listar_clientes')


class EliminarCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cine/cliente/eliminar_cliente.html'
    success_url = reverse_lazy('cine:listar_clientes')

    def get_context_data(self, *args, **kwargs):
        cliente = Cliente.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarCliente, self).get_context_data(*args, **kwargs)
        context['cliente'] = cliente
        return context

# View Reserva

class ListarReservas(ListView):
    model = Reserva
    template_name = 'cine/reserva/listar_reserva.html'
    queryset = Reserva.objects.all()
    context_object_name = 'reservas'

class CrearReserva(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'cine/reserva/crear_reserva.html'
    success_url = reverse_lazy('cine:listar_reservas')

class EditarReserva(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'cine/reserva/editar_reserva.html'
    success_url = reverse_lazy('cine:listar_reservas')


class EliminarReserva(DeleteView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'cine/reserva/eliminar_reserva.html'
    success_url = reverse_lazy('cine:listar_reservas')

    def get_context_data(self, *args, **kwargs):
        reserva = Reserva.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarReserva, self).get_context_data(*args, **kwargs)
        context['reserva'] = reserva
        return context