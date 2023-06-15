from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone




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

class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score1 = models.CharField(max_length=20, null=True, blank=True)
    score2 = models.CharField(max_length=20, null=True, blank=True)
    score3 = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.first_name