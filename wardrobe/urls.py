from django.urls import path 
from wardrobe.apps import WardrobeConfig
from wardrobe.views import (
    WardrobeView, 
    WardrobeSaveOrderView,
    WardrobeOrderDetailView, 
    combination_not_found_view, 
    save_order_success_view, 
    wardrobe_orders_list_view, 
    wardrobe_order_delete_view, 
    WardrobeOrderUpdateView, 
    wardrobe_deactivated_list_view,
    toggle_order_active_view,
    WardrobeDeactivatedDetailView,
)

app_name = WardrobeConfig.name


urlpatterns = [
    path('calculator/', WardrobeView.as_view(), name='calculator'),
    path('combination_not_found/', combination_not_found_view, name='combination_not_found'),
    path('save_order/', WardrobeSaveOrderView.as_view(), name='save_order'),
    path('save_order_success/', save_order_success_view, name='save_order_success'),
    path('orders/', wardrobe_orders_list_view, name='show_wardrobe_orders'),
    path('order_detail/<int:pk>/', WardrobeOrderDetailView.as_view(), name='show_wardrobe_order_detail'), 
    path('order_delete/<int:pk>/', wardrobe_order_delete_view, name='order_delete'),
    path('order_update/<int:pk>/', WardrobeOrderUpdateView.as_view(), name='wardrobe_order_update'),
    # management
    path('management/wardrobe-deactivated/', wardrobe_deactivated_list_view, name='wardrobe_deactivated'),
    path('management/togggle-order-activity/<int:pk>/', toggle_order_active_view, name='toggle_order_activity'),
    path('management/wardrobe-deactivated-details/<int:pk>/', WardrobeDeactivatedDetailView.as_view(), name='wardrobe_deactivated_details'),
]
