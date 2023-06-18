"""
URL configuration for Atletapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from Planificaciones.views import inicio, about_dr
from django.conf import settings
from django.conf.urls.static import static
#from .views import about_me

urlpatterns = [
    path("inicio", inicio, name="inicio" ),
    path('admin/', admin.site.urls),
    path("planificaciones/", include("Planificaciones.urls")),
    path("atletas/", include("Atletas.urls")),
    path("drdevs/", about_dr, name="about_dr"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
