from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CountrySerializer
from .models import Country


class CountryViewSet(viewsets.ViewSet):
    """
    
    """

    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()

    def get_object(self, pk):
        return get_object_or_404(Country, pk=pk)

    def save_object(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        """ List all countries """
        queryset = self.get_queryset()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = self.get_object(pk=pk)
        serializer = CountrySerializer(instance=instance)
        return Response(serializer.data)
    
    def create(self, request):
        """ Save a new country """
        serializer = CountrySerializer(data=request.data)
        return self.save_object(serializer) 

    def update(self, request, pk=None):
        instance = self.get_object(pk=pk)
        serializer = CountrySerializer(instance, data=request.data)
        return self.save_object(serializer)

    def destroy(self, request, pk=None):
        instance = self.get_object(pk=pk)
        instance.delete()
        return Response(status=200)
