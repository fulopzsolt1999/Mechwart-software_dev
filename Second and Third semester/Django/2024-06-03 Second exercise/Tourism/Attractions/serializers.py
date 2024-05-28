from rest_framework import serializers
from .models import TourismAttractions

class TourismAttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismAttractions
        fields = "__all__"
        depth = 2