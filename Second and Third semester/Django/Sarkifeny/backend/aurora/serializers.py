from rest_framework import serializers
from .models import Observation, City

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = "__all__"
        depth = 1

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"