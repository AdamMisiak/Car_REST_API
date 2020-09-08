from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from cars.models import Car

User = get_user_model()


class CarAPITestCase(APITestCase):
	def setUp(self):
		user_obj = User.objects.create(username='test', email='test@test.com')
		user_obj.set_password("testtest")
		user_obj.save()
		car = Car.objects.create(
			user=user_obj, model='test', brand='test', color='test', horsepower=420
		)

	def test_user(self):
		user_count = User.objects.count()
		assert user_count == 1

	def test_car(self):
		car_count = Car.objects.count()
		assert car_count == 1