from django.db import models

# Create your models here.
class Szak(models.Model):
   szakNev = models.CharField(max_length=200)
   tamogatott = models.BooleanField()

class Felvetelizo(models.Model):
   szak = models.ForeignKey(Szak, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   szul_ev = models.DateField()
   pontszam = models.IntegerField()
   