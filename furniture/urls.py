from django.urls import path
from furniture.apps import FurnitureConfig
from furniture.views import IndexView

app_name = FurnitureConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
