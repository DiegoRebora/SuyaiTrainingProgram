from django.contrib import admin
from django.urls import path
from django.contrib import admin
from Atletas.views import *

urlpatterns = [
    path("registro/", registro, name="registro" ),
    path("login/", login_view, name="login" ),
    path("logout/", CustomLogoutView.as_view(), name="logout" ),
    path("profile/", MiPerfilUpdateView.as_view(), name="editar_usuario" ),
    path("agregar_avatar/", agregar_avatar, name="agregar_avatar" ),
    path("crear_atleta/", AtletaCreateView.as_view(), name="crear_atleta"),
    path("editar_atleta/<int:pk>/", AtletaUpdateView.as_view(), name="editar_atleta"),
    path("ver_atleta/<int:pk>/", AtletaDetailView.as_view(), name="ver_atleta"),
    path("listar_atletas/", AtletaListView.as_view(), name="listar_atletas"),
    path("buscar_atleta/", AtletaSearchView. as_view(), name="buscar_atleta"),
    path("crear_score/", ScoreCreateView.as_view(), name="crear_score"),
    path("listar_scores/", ScoreListView.as_view(), name="listar_scores"),
    path("buscar_score/", ScoreSearchView. as_view(), name="buscar_score"),
    path("crear_planificacion/", PlanificacionesCreateView .as_view(), name="crear_plani"),
    path("listar_planificaciones/", PlanificacionesListView.as_view(), name="listar_planis"),
    path("editar_planificacion/<int:pk>/", PlanificacionesUpdateView.as_view(), name="editar_plani"),
    path("borrar_planificacion/<int:pk>/", PlanificacionesDeleteView.as_view(), name="borrar_plani"),
    path("ver_planificacion/<int:pk>/", PlanificacionesDetailView.as_view(), name="ver_plani"),
    path("buscar_planificacion/", PlanificacionesSearchView. as_view(), name="buscar_plani"),

]
