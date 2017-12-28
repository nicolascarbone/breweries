from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CitySerializer
from .models import City


class CityViewSet(viewsets.ViewSet):
    """
    
    """

    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.all()

    def get_object(self, pk):
        return get_object_or_404(City, pk=pk)

    def save_object(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        """ List all countries """
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = self.get_object(pk=pk)
        serializer = CitySerializer(instance=instance)
        return Response(serializer.data)
    
    def create(self, request):
        """ Save a new City """
        serializer = CitySerializer(data=request.data)
        return self.save_object(serializer) 

    def update(self, request, pk=None):
        instance = self.get_object(pk=pk)
        serializer = CitySerializer(instance, data=request.data)
        return self.save_object(serializer)

    def destroy(self, request, pk=None):
        instance = self.get_object(pk=pk)
        instance.delete()
        return Response(status=200)
