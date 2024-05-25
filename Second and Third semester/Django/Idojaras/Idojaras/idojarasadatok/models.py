from django.db import models

# Create your models here.
class Meres(models.Model):
   varos=models.CharField(max_length=100)
   utca=models.CharField(max_length=100, default="X")
   ertek=models.FloatField()
   idopont=models.DateTimeField()

   class Meta:
      verbose_name_plural = 'Mérések'

   def __str__(self):
       return f'{self.varos}, {self.idopont}'
   