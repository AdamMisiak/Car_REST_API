from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Car(models.Model):
    # driver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
