from rest_framework import serializers
from .models import Clothing


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['id', 'size', 'color', 'kind', 'name', 'price', 'discount', 'image']