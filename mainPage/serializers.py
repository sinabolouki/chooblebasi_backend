from item.models import Clothing
from rest_framework import serializers


class MainPageClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['id', 'price', 'image', 'name']