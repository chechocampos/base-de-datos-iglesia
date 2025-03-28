from django.urls import path
from .views import (
    lista_iglesias,
    lista_feligreses,
    detalle_feligres,
    editar_feligres,
    eliminar_feligres,
    agregar_feligres
)

urlpatterns = [
    path('', lista_iglesias, name='lista_iglesias'),  # Esta es la raíz: lista de iglesias
    path('<int:iglesia_id>/', lista_feligreses, name='lista_feligreses'),
    path('<int:iglesia_id>/<int:feligres_id>/', detalle_feligres, name='detalle_feligres'),
    path('<int:iglesia_id>/<int:feligres_id>/editar/', editar_feligres, name='editar_feligres'),
    path('<int:iglesia_id>/<int:feligres_id>/eliminar/', eliminar_feligres, name='eliminar_feligres'),
    path('<int:iglesia_id>/agregar/', agregar_feligres, name='agregar_feligres'),
]
