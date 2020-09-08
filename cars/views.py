from rest_framework import mixins
from rest_framework import generics
from cars.models import Car
from cars.serializers import CarSerializer
from django.db.models import Q


# class CarsList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):

class CarsList(generics.ListCreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


    #http://127.0.0.1:8000/cars/?q=Audi
    def get_queryset(self):
        queryset = Car.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(Q(model__icontains=query)|Q(brand__icontains=query)).distinct()
        return queryset

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


# class CarDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):

class CarDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)