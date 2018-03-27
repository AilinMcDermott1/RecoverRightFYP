from rest_framework import serializers
from .models import savedNutrition

class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = savedNutrition
