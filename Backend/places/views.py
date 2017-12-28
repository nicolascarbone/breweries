from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PlaceSerializer
from .models import Place


class PlaceViewSet(viewsets.ViewSet):
    """
    
    """

    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.all()

    def save_object(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        """ List all places """
        queryset = self.get_queryset()
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(Place, pk=pk)
        serializer = PlaceSerializer(instance=instance)
        return Response(serializer.data)
    
    def create(self, request):
        """ Save a new place """
        serializer = PlaceSerializer(data=request.data)
        return self.save_object(serializer) 

    def update(self, request, pk=None):
        instance = get_object_or_404(Place, pk=pk)
        serializer = PlaceSerializer(instance, data=request.data)
        return self.save_object(serializer)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(Place, pk=pk)
        instance.delete()
        return Response(status=200)
