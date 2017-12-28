from rest_framework import serializers, viewsets

from .models import Recipe


class RecipeSerializer(viewsets.ModelSerializer):

    class Meta:
        model = Recipe 