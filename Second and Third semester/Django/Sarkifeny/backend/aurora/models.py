from django.db import models
from datetime import datetime

class Observation(models.Model):
   city=models.ForeignKey("City",on_delete=models.CASCADE)
   street=models.CharField(max_length=150, null=False)
   observTime=models.DateTimeField(default=datetime.now())
   auroraType=models.CharField(max_length=100)

   class Meta:
      verbose_name_plural = 'Observations'

   def __str__(self):
       return f'{self.city.city}, {self.street}, {self.auroraType}'
   
class City(models.Model):
   city=models.CharField(max_length=150, null=False)

   class Meta:
      verbose_name_plural = 'Cities'

   def __str__(self):
       return self.city