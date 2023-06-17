from django.contrib import admin
from .models import Atleta, Score, Planificaciones, Avatar
# Register your models here.
admin.site.register(Atleta)
admin.site.register(Score)
admin.site.register(Planificaciones)
admin.site.register(Avatar)