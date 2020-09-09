from django.db import models
from django.contrib.auth.models import User
from rest_framework.reverse import reverse as api_reverse


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    horsepower = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model}"

    @property
    def owner(self):
        return self.user

    def get_api_url(self):
        return api_reverse("cars:car-detail", kwargs={"pk": self.pk})
