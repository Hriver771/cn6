from rest_framework import serializers
from .models import Stones

class StoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stones
        fields = ('x1', 'y1', 'x2', 'y2')
