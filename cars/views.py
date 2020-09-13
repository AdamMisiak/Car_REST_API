from rest_framework import generics
from cars.models import Car
from django.contrib.auth.models import User
from cars.serializers import CarSerializer, UserFullSerializer
from cars.permissions import IsOwnerOrReadOnly
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cars': reverse('cars:cars-list', request=request, format=format),
        'users': reverse('cars:users-list', request=request, format=format)
    })


class CarsList(generics.ListCreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # http://127.0.0.1:8000/cars/?q=Audi
    def get_queryset(self):
        queryset = Car.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(
                Q(model__icontains=query) | Q(brand__icontains=query)
            ).distinct()
        return queryset

    # aktualny user przypisany do auta
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UsersList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserFullSerializer

    # http://127.0.0.1:8000/users/?q=adam
    def get_queryset(self):
        queryset = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(
                Q(username__icontains=query) | Q(email__icontains=query)
            ).distinct()
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserFullSerializer

