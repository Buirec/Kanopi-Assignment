from rest_framework import serializers
from app.models import ColourType

class ColourRequestSerializer(serializers.Serializer):
  type = serializers.CharField(max_length=4)

class ColourTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ColourType
    fields = ['colour_type', 'first_value', 'second_value', 'third_value', 'first_value_max', 'second_value_max', 'third_value_max']
