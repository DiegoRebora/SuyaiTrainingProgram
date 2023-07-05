# URL configuration for Atletapp project.
# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path, include
from Planificaciones.views import inicio, about_dr, about_us, about_hc
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path("planificaciones/", include("Planificaciones.urls")),
    path("atletas/", include("Atletas.urls")),
    path("drdevs/", about_dr, name="about_dr"),
    path("sobre_nosotros/", about_us, name="about_us"),
    path("sobre_seba/", about_hc, name="about_hc"),
    path('recuperar-contraseña/',
         auth_views.PasswordResetView.as_view(
             template_name='registration\password_reset_form.html',
             email_template_name='registration\password_reset_email.html',
             subject_template_name='registration\password_reset_subject.txtt'
         ),
         name='password_reset'),
    path('recuperar-contraseña/enviado/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration\password_reset_done.html'
         ),
         name='password_reset_done'),
    path('recuperar-contraseña/confirmar/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration\password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('recuperar-contraseña/completado/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration\password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
