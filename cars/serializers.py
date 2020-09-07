from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Car
            fields = ['id', 'model', 'brand', 'color', 'horsepower']