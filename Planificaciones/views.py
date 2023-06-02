from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from typing import Dict
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Planificaciones.models import Planificacion

def inicio(request):
    contexto = {}
    return render(
        request=request,
        template_name='Planificaciones/inicio.html',
        context=contexto,
    )


class PlanificacionListView(LoginRequiredMixin, ListView):
    model = Planificacion
    template_name = 'Planificaciones/planificacion.html'
    context_object_name = 'planis'
    #login_url = 'login'

class PlanificacionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Planificacion
    template_name = 'Planificaciones/planificacion_form.html'
    fields = ['semana', 'descripcion', 'fecha_inicio', 'coach', 'planificacion', 'comentario']
    success_url = reverse_lazy('listar_planis')
    #login_url = 'login'
    permission_required = 'Planificaciones.add_planificacion'

    def form_valid(self, form):
        form.instance.planificacion = self.request.FILES.get('planificacion')
        return super().form_valid(form)
    
class PlanificacionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Planificacion
    template_name = 'Planificaciones/planificacion_form.html'
    fields = ['semana', 'descripcion', 'fecha_inicio', 'coach', 'planificacion', 'comentario']
    success_url = reverse_lazy('planificacion_listar')
    #login_url = 'login'
    permission_required = 'Planificaciones.change_planificacion'

    def form_valid(self, form):
        form.instance.planificacion = self.request.FILES.get('planificacion')
        return super().form_valid(form)

class PlanificacionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Planificacion
    template_name = 'Planificaciones/planificacion_confirm_delete.html'
    success_url = reverse_lazy('listar_planis')
    #login_url = 'login'
    permission_required = 'Planificaciones.delete_planificacion'

class PlanificacionDetailView(LoginRequiredMixin, DetailView):
    model = Planificacion
    success_url = reverse_lazy('listar_planis')
    #login_url = 'login'
