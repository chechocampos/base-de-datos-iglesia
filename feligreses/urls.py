from django.urls import path
from .views import lista_iglesias, lista_feligreses, editar_feligres, eliminar_feligres, agregar_feligres

urlpatterns = [
    path('', lista_feligreses, name='lista_feligreses'),
    path('<int:feligres_id>/', detalle_feligres, name='detalle_feligres'),
    path('<int:feligres_id>/editar/', editar_feligres, name='editar_feligres'),
    path('<int:feligres_id>/eliminar/', eliminar_feligres, name='eliminar_feligres'),
    path('agregar/', agregar_feligres, name='agregar_feligres'),
]
