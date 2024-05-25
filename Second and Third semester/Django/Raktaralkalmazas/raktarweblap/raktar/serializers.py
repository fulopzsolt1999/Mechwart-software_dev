from rest_framework import serializers
from .models import Termek

class TermekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termek
        fields = "__all__"
        depth=1