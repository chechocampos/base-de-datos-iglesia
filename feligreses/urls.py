from django.urls import path
from .views import (
    lista_hermanos,
    detalle_hermano,
    agregar_hermano,
    editar_hermano,
    eliminar_hermano,
)

urlpatterns = [
    path('', lista_hermanos, name='lista_hermanos'),
    path('<int:pk>/', detalle_hermano, name='detalle_hermano'),
    path('nuevo/', agregar_hermano, name='agregar_hermano'),  # ✅ ESTA es la que usarás
    path('editar/<int:pk>/', editar_hermano, name='editar_hermano'),
    path('eliminar/<int:pk>/', eliminar_hermano, name='eliminar_hermano'),
]
