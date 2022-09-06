from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal
from .serializers import MealSerializer
from .models import Ingredient
from .serializers import IngredientSerializer
from .models import DayData
from .serializers import DayDataSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

class DayDataViewSet(viewsets.ModelViewSet):

    queryset = DayData.objects.all()
    serializer_class = DayDataSerializer

    @action(detail=False)
    def lastDayData(self, request):
        #lastDayData = DayData.objects.all().order_by('-id')     
        queryset = DayData.objects.last()
        serializer_class = DayDataSerializer(queryset)
        return Response(serializer_class.data)

