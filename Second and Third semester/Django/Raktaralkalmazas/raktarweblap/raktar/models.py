from django.db import models

# Create your models here.
class Kategoria(models.Model):
    kategoriaNev=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.kategoriaNev

class Termek(models.Model):
    termekNev=models.CharField(max_length=100)
    ar=models.IntegerField()
    db=models.IntegerField()
    kategoria=models.ForeignKey("Kategoria", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.termekNev