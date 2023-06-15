from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView, DetailView, ListView, DeleteView

from Atletas.forms import UserRegisterForm, UserUpdateForm,  AtletaForm, AtletaUpdateForm, AvatarFormulario, ScoreForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from Atletas.models import Avatar, Atleta, Score
# Create your views here.
def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  
           url_exitosa = reverse('login')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='Atletas/registro.html', 
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='Atletas/login.html',
       context={'form': form},
   )

class CustomLogoutView(LogoutView):
   template_name = 'Atletas/logout.html' 

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   model = User
   form_class = UserUpdateForm
   success_url = reverse_lazy('listar_atletas')
   template_name = 'Atletas/formulario_perfil.html'
   def get_object(self):
        return self.request.user  ##CREAR HTML


class AtletaCreateView(LoginRequiredMixin, CreateView):
    model = Atleta
    form_class = AtletaForm
    template_name = "Atletas/formulario_atleta.html"
    success_url = reverse_lazy("listar_atletas")

    def get_object(self, queryset=None):
        # Obtener el objeto Atleta existente del usuario actual o crear uno nuevo
        obj, created = self.model.objects.get_or_create(user=self.request.user)
        return obj

    def form_valid(self, form):
        # Asignar el usuario actual al objeto Atleta
        form.instance.user = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # Verificar si se está creando un nuevo objeto Atleta o editando uno existente
        if self.kwargs.get('pk'):
            # Si se está editando, continuar con el flujo normalmente
            return super().dispatch(request, *args, **kwargs)
        else:
            # Si se está creando un nuevo objeto, redirigir a la vista de edición con el objeto existente
            atleta_existente = self.get_object()
            return redirect('editar_atleta', pk=atleta_existente.pk)

class AtletaUpdateView(LoginRequiredMixin, UpdateView):
    model = Atleta
    form_class = AtletaForm
    template_name = "Atletas/formulario_atleta.html"
    success_url = reverse_lazy("listar_atletas")

    def get_object(self):
        # Obtener el objeto Atleta del usuario actual
        obj = Atleta.objects.get(user=self.request.user)
        return obj

class AtletaListView(ListView):
    model = Atleta
    template_name = 'Atletas/atletas.html'


class AtletaSearchView(LoginRequiredMixin, ListView):
    model = Atleta
    template_name = 'Atletas/atletas.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Atleta.objects.filter(user__first_name__icontains=query)
        return object_list

class AtletaDetailView(LoginRequiredMixin, DetailView):
    model = Atleta
    template_name = "Atletas/atleta_detail.html"



def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar, created = Avatar.objects.get_or_create(user=request.user)
            
            if form.cleaned_data['imagen']:
                avatar.imagen = form.cleaned_data['imagen']
            else:
                
                avatar.imagen = 'avatares/default_avatar.jpg'
                print(avatar.imagen)
            avatar.save()
            return redirect('inicio')
    else:
        form = AvatarFormulario()
    return render(request, 'Atletas/agregar_avatar.html', {'form': form})

class ScoreCreateView(CreateView):
    model = Score
    form_class = ScoreForm
    template_name = 'Atletas/score.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ScoreCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.now()
        return super().form_valid(form)
    
