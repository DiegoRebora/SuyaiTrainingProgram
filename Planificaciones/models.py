from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class Planificacion(models.Model):
    semana = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    coach = models.CharField(max_length=255)
    comentario = models.TextField(blank=True)
    

    def __str__(self):
        return f"Semana {self.semana}: {self.descripcion}"

