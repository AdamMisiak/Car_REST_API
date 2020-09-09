from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = ["url", "id", "user", "model", "brand", "color", "horsepower", "added"]
        read_only_fields = ["id", "user", "added"]

    def get_url(self, obj):
        return obj.get_api_url()

    # walidacja czy taki model istnieje + wykluczenie siebie samego z queryset
    def validate_model(self, value):
        queryset = Car.objects.filter(model__iexact=value)
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise serializers.ValidationError("The model of car has already been used!")
        return value
