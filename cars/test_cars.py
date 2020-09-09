from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from cars.models import Car

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

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

	def test_get_list(self):
		data = {}
		url = api_reverse('cars:cars-list')
		response = self.client.get(url, data, format='json')
		assert response.status_code == status.HTTP_200_OK

	def test_post_item(self):
		data = {'model': 'test2', 'brand': 'test2', 'color': 'test2', 'horsepower': 123}
		url = api_reverse('cars:cars-list')
		response = self.client.post(url, data, format='json')
		assert response.status_code == status.HTTP_401_UNAUTHORIZED

	def test_get_item(self):
		car = Car.objects.first()
		data = {}
		url = car.get_api_url()
		response = self.client.get(url, data, format='json')
		assert response.status_code == status.HTTP_200_OK

	def test_update_item(self):
		car = Car.objects.first()
		url = car.get_api_url()
		data = {'model': 'test23', 'brand': 'test23', 'color': 'test23', 'horsepower': 1235}
		response = self.client.post(url, data, format='json')
		response2 = self.client.put(url, data, format='json')
		assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
		assert response2.status_code == status.HTTP_401_UNAUTHORIZED

	def test_update_item_with_user(self):
		car = Car.objects.first()
		url = car.get_api_url()
		user_obj = User.objects.first()
		data = {'model': 'test23', 'brand': 'test23', 'color': 'test23', 'horsepower': 1235}

		payload = payload_handler(user_obj)
		token_response = encode_handler(payload)
		self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)  # JWT <token> dodanie tokena do autoryzacji https://jpadilla.github.io/django-rest-framework-jwt/

		response = self.client.put(url, data, format='json')
		#print(response.data)
		assert response.status_code == status.HTTP_200_OK

	def test_post_item_with_user(self):
		user_obj = User.objects.first()
		data = {'model': 'test2', 'brand': 'test2', 'color': 'test2', 'horsepower': 123}

		payload = payload_handler(user_obj)
		token_response = encode_handler(payload)
		self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)

		url = api_reverse('cars:cars-list')
		response = self.client.post(url, data, format='json')
		assert response.status_code == status.HTTP_201_CREATED

	def test_user_ownership(self):
		# przypisanie auta do ownera
		owner = User.objects.create(username='testuser2')
		car = Car.objects.create(
			user=owner, model='test', brand='test', color='test', horsepower=420
		)
		user_obj = User.objects.first()
		assert user_obj.username != owner.username

		# autoryzacja nowego usera
		payload = payload_handler(user_obj)
		token_rsp = encode_handler(payload)
		self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)

		url = car.get_api_url()
		data = {'model': 'test2', 'brand': 'test2', 'color': 'test2', 'horsepower': 123}
		# aktulizacja samochodu jako nie-owner
		response = self.client.put(url, data, format='json')
		assert response.status_code == status.HTTP_403_FORBIDDEN