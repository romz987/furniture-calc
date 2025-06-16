from django.urls import path 
from wardrobe.apps import WardrobeConfig
from wardrobe.views import wardrobe

app_name = WardrobeConfig.name


urlpatterns = [
    path('wardrobe/', wardrobe, name='calculator'),
]
