from rest_framework import serializers
from .models import Meal
from .models import Ingredient
from .models import DayData


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DayDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayData
        fields = '__all__'
