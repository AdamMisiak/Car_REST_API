from django.db import models


class Car(models.Model):
	added = models.DateTimeField(auto_now_add=True)
	model = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	horsepower = models.IntegerField()
