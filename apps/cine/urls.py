from django.urls import path
from .views import crear_compra
from .views import listar_compras


urlpatterns = [
    path('listar_compras/', listar_compras, name='listar_compras'),
    path('crear_compra/', crear_compra, name='crear_compra')
]
