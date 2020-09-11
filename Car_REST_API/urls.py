from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from cars import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('cars.urls')),
    path('', views.api_root),
]