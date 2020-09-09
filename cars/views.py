from rest_framework import generics
from cars.models import Car
from cars.serializers import CarSerializer
from cars.permissions import IsOwnerOrReadOnly
from django.db.models import Q


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

