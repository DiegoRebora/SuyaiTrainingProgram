from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.views.generic.edit import FormView



def inicio(request):
    contexto = {}
    return render(
        request=request,
        template_name='Planificaciones/inicio.html',
        context=contexto,
    )

def about_dr(request):
    return render(request, 'Planificaciones/about_dr.html')

def about_us(request):
    return render(request, 'Planificaciones/about_us.html')

def about_hc(request):
    return render(request, 'Planificaciones/about_hc.html')


class PasswordResetView(FormView):
    template_name = 'registration\password_reset_form.html'
    form_class = PasswordResetForm
    success_url = '/recuperar-contraseña/enviado/'

    def form_valid(self, form):
        """
        If the form is valid, send a password reset email to the user.
        """
        form.save(
            domain_override=self.request.META['HTTP_HOST'],
            use_https=self.request.is_secure(),
            request=self.request,
        )
        return super().form_valid(form)
    