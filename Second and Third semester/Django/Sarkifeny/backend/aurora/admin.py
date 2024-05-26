from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Observation)
admin.site.register(models.City)