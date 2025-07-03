from django.urls import path
from furniture.apps import FurnitureConfig
from furniture.views import (
    IndexView,
    wardrobe_man_view,
    dresser_man_view,
    kitchen_man_view,
    # заглушки
    dresser_calc_plug_view,
    kitchen_calc_plug_view,
    dresser_orders_plug_view,
    kitchen_orders_plug_view,
)

app_name = FurnitureConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # мануалы
    path('wardrobe-manual/', wardrobe_man_view, name='wardrobe_manual'),
    path('dresser-manual/', dresser_man_view, name='dresser_manual'),
    path('kitchen-manual/', kitchen_man_view, name='kitchen_manual'),
    # заглушки калькуляторы
    path('dresser-calc-plug/', dresser_calc_plug_view, name='dresser_calc_plug'),
    path('kitchen-calc-plug/', kitchen_calc_plug_view, name='kitchen_calc_plug'),
    # заглушки заказы
    path('dresser-orders-plug/', dresser_orders_plug_view, name='dresser_orders_plug'),
    path('kitchen-orders-plug/', kitchen_orders_plug_view, name='kitchen_orders_plug'),
]
