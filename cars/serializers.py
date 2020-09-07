from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Car
            fields = ['id', 'model', 'brand', 'color', 'horsepower', 'added']
            read_only_fields = ['added']

        def validate_model(self, value):
            queryset = Car.objects.filter(model__iexact=value)
            if self.instance:
                queryset = queryset.exclude(id=self.instance.id)
            if queryset.exists():
                raise serializers.ValidationError('The model of car has already been used!')
            return value