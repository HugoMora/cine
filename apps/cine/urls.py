from django.urls import path
from .views import listar_compras
from .views import crear_compra
from .views import eliminar_compra
from .views import actualizar_compra


urlpatterns = [
    path('listar_compras/', listar_compras, name='listar_compras'),
    path('eliminar_compra/', eliminar_compra, name='eliminar_compra'),
    path('actualizar_compra/', actualizar_compra, name='actualizar_compra'),
    path('crear_compra/', crear_compra, name='crear_compra')
]
