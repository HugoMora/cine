from django.urls import path
from .views import listar_reservas
from .views import listar_clientes
from .views import crear_cliente
from .views import crear_reserva


urlpatterns = [
    path('listar_reservas/', listar_reservas, name='listar_reservas'),
    path('crear_reserva/', crear_reserva, name='crear_reserva'),
    path('listar_clientes/', listar_clientes, name='crear_clientes'),
    path('crear_cliente/', crear_cliente, name='crear_cliente')
]
