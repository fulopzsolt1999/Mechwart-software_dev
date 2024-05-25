from rest_framework import serializers
from .models import Meres

class MeresSerializer(serializers.ModelSerializer):
   class Meta:
      model = Meres
      fields = '__all__'