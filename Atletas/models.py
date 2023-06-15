from django.db import models

# Create your models here.
from django.contrib.auth.models import User




class Avatar(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  
   imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

   def __str__(self):
       return f"Avatar de: {self.user}"
   
"""class Atleta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, null=True, blank=True)
    apodo = models.CharField(max_length=20, null=True,  blank=True)

    def __str__(self):
        return self.user.username"""

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
        return self.apodo
