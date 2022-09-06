from django.urls import path, include
from rest_framework import routers
from restapi.views import MealViewSet, IngredientViewSet, DayDataViewSet

meals_router = routers.SimpleRouter()
meals_router.register(
    r'meals',
    MealViewSet,
    basename='meal',
)

ingredients_router = routers.SimpleRouter()
ingredients_router.register(
    r'ingredients',
    IngredientViewSet,
    basename='ingredient',
)

daydata_router = routers.SimpleRouter()
daydata_router.register(
    r'daydata',
    DayDataViewSet,
    basename='daydata',
)

daydata_list = DayDataViewSet.as_view({
    'get': 'list'
})

daydata_retrieveLast = DayDataViewSet.as_view({
    'get': 'retrieveLast'
})

urlpatterns = [
    # Admin routes are registered here

    # API
    path('api/', include(meals_router.urls)),
    path('api/', include(ingredients_router.urls)),
    path('api/', include(daydata_router.urls)),
]
