from django.urls import path
from furniture.apps import FurnitureConfig
from furniture.views import FurnitureListView

app_name = FurnitureConfig.name


urlpatterns = [
    path('', FurnitureListView.as_view(), name='index'),
]
