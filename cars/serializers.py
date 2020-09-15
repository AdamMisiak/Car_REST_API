from rest_framework import serializers
from cars.models import Car
from django.contrib.auth.models import User


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "is_superuser",
        ]
        read_only_fields = ["id", "date_joined", "is_superuser"]


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=True)
    username = serializers.CharField(max_length=100)


class CarSerializer(serializers.ModelSerializer):
    # dodac w fields url
    url = serializers.SerializerMethodField(read_only=True)

    # dodatkowy serializer do podania info o userze
    # user = UserSerializer(required=False)

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
