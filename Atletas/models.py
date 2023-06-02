from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Atleta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    categoria = models.CharField(max_length=20, null=True, blank=True)
    apodo = models.CharField(max_length=20, null=True, blank=True)
    Fran = models.DurationField( null=True, blank=True)
    Grace = models.DurationField( null=True, blank=True)
    Isabel = models.DurationField( null=True, blank=True)
    Murph = models.DurationField( null=True, blank=True)   
    RM_backsquat = models.IntegerField( null=True, blank=True)
    RM_deadlift = models.IntegerField(null=True, blank=True)
    RM_bench = models.IntegerField(null=True, blank=True)
    RM_snatch = models.IntegerField(null=True, blank=True)
    RM_clean = models.IntegerField(null=True, blank=True)
    RM_jerk = models.IntegerField(null=True, blank=True)
    RM_cleanandjerk = models.IntegerField(null=True, blank=True)
  




class Avatar(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  
   imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

   def __str__(self):
       return f"Avatar de: {self.user}"
   
