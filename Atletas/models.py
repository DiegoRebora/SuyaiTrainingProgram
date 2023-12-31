from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import DateInput




class Avatar(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  
   imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

   def __str__(self):
       return f"Avatar de: {self.user}"


class Atleta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  default=1)
    categoria = models.CharField(max_length=20, null=True, blank=True)
    apodo = models.CharField(max_length=20, null=True,  blank=True)
    grace = models.CharField(max_length=20, null=True, blank=True)
    fran = models.CharField(max_length=20, null=True, blank=True)
    murph = models.CharField(max_length=20, null=True, blank=True)
    backsquat_rm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    clean_rm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    jerk_rm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    snatch_rm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    deadlift_rm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.apodo or self.user.username

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score1 = models.CharField(max_length=20, null=True, blank=True)
    score2 = models.CharField(max_length=20, null=True, blank=True)
    score3 = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.user.first_name
    
class Planificaciones(models.Model):
    fecha_inicio = models.DateField()
    numero_semana = models.IntegerField()
    imagen_planificacion = models.ImageField(upload_to='planificaciones/')
    comentario = models.CharField(max_length=255)
    def __str__(self):
        return str(self.numero_semana)
