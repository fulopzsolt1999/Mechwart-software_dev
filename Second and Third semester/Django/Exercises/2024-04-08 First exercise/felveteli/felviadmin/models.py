from django.db import models

# Create your models here.
class Szak(models.Model):
   szakNev = models.CharField(max_length=100)

   def __str__(self) -> str:
        return self.szakNev

class Felvetelizo(models.Model):
    nev = models.CharField(max_length=100)
    szul_ev = models.IntegerField()
    pontszam = models.IntegerField()
    szak = models.ForeignKey(Szak, on_delete=models.CASCADE)