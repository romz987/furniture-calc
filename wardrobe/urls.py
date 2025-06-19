from django.urls import path 
from wardrobe.apps import WardrobeConfig
from wardrobe.views import wardrobe, WardrobeView, combination_not_found

app_name = WardrobeConfig.name


urlpatterns = [
    path('wardrobe/', WardrobeView.as_view(), name='calculator'),
    path('combination_not_found/', combination_not_found, name='combination_not_found'),
]
