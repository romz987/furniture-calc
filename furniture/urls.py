from django.urls import path
from furniture.apps import FurnitureConfig
from furniture.views import index 

app_name = FurnitureConfig.name

urlpatterns = [
    path('', index , name='index')
]
