from django.contrib import admin
from django.urls import path
from Planificaciones.views import *
from django.urls import path
from .views import *

app_name = 'planificaciones'

urlpatterns = [
    path("", PlanificacionListView.as_view(), name="listar_planis" ),
    path("crear-planis/", PlanificacionCreateView.as_view(), name="crear_plani" ),
    path("ver-planis/<int:pk>/", PlanificacionDetailView.as_view(), name="ver_plani" ),
    path("editar-plani/<int:pk>/", PlanificacionUpdateView.as_view(), name="editar_plani" ),
    path("borrar-plani/<int:pk>/", PlanificacionDeleteView.as_view(), name="borrar_plani" ),
    #path("buscar-circuitos/", SearchCircuito.as_view(), name="buscar_circuito" ),
]
