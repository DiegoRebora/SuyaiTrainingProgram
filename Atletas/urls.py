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
]
