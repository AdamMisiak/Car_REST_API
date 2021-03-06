from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views

app_name = "cars"

urlpatterns = [
    path("cars/", views.CarsList.as_view(), name="cars-list"),
    path("cars/<int:pk>/", views.CarDetail.as_view(), name="car-detail"),
    path("users/", views.UsersList.as_view(), name="users-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
