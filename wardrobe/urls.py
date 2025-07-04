from django.urls import path 
from wardrobe.apps import WardrobeConfig
from wardrobe.views import WardrobeView, WardrobeSaveOrderView, WardrobeOrderDetailView, combination_not_found_view, save_order_success_view, orders_list_view, order_delete_view, OrderUpdateView

app_name = WardrobeConfig.name


urlpatterns = [
    path('calculator/', WardrobeView.as_view(), name='calculator'),
    path('combination_not_found/', combination_not_found_view, name='combination_not_found'),
    path('save_order/', WardrobeSaveOrderView.as_view(), name='save_order'),
    path('save_order_success/', save_order_success_view, name='save_order_success'),
    path('orders/', orders_list_view, name='show_wardrobe_orders'),
    path('order_detail/<int:pk>/', WardrobeOrderDetailView.as_view(), name='show_wardrobe_order_detail'), 
    path('order_delete/<int:pk>/', order_delete_view, name='order_delete'),
    path('order_update/<int:pk>/', OrderUpdateView.as_view(), name='wardrobe_order_update')
]
