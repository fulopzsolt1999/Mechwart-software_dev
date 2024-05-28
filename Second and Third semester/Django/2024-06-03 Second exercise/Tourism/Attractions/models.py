from django.db import models

class Countries(models.Model):
   name = models.CharField(max_length=200)

   class Meta:
      verbose_name_plural = 'Országok'

   def __str__(self):
       return self.name

class Cities(models.Model):
   name = models.CharField(max_length=200)
   country = models.ForeignKey(Countries, on_delete=models.CASCADE, default="")

   class Meta:
      verbose_name_plural = 'Városok'

   def __str__(self):
       return self.name


class TourismAttractions(models.Model):
   city = models.ForeignKey(Cities, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   short_description = models.CharField(max_length=200)
   average_rate = models.DecimalField(max_digits=3, decimal_places=2)
   opening_hours = models.CharField(max_length=200)

   def save(self, *args, **kwargs):
      self.average_rate = round(self.average_rate, 2)
      super(TourismAttractions, self).save(*args, **kwargs)

   class Meta:
      verbose_name_plural = 'Turisztikai Látványosságok'

   def __str__(self):
       return f'{self.city}, {self.name}'