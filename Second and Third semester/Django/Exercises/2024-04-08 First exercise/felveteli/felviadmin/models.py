from django.db import models

# Create your models here.
class Szak(models.Model):
   szakNev = models.CharField(max_length=200)

   def __str__(self):
      return f"{self.szakNev}"

class Felvetelizo(models.Model):
   szak = models.ForeignKey(Szak, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   szul_ev = models.IntegerField()
   pontszam = models.IntegerField()
   