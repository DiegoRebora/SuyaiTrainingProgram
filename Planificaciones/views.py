from django.shortcuts import render


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