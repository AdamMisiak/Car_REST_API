from django.urls import path, include

urlpatterns = [
    path('', include('cars.urls')),
]