from django.urls import path 
from reference.apps import ReferenceConfig 
from reference.views import (
    boxsummary_show_view, 
    BoxSummaryUpdateView, 
    boxsummary_delete_view, 
    BoxSummaryCreateView, 
    doorsummary_show_view, 
    DoorSummaryUpdateView, 
    doorsummary_delete_view, 
    DoorSummaryCreateView,
)

app_name = ReferenceConfig.name


urlpatterns = [
    # box_summary
    path('box_summary_create', BoxSummaryCreateView.as_view(), name='ref_boxsummary_create'),
    path('box_summary/', boxsummary_show_view, name='ref_boxsummary'),
    path('box_summary_update/<int:pk>', BoxSummaryUpdateView.as_view(), name='ref_boxsummary_update'),
    path('box_summary_delete/<int:pk>', boxsummary_delete_view, name='ref_boxsummary_delete'),
    # door_summary
    path('door_summary_create', DoorSummaryCreateView.as_view(), name='ref_doorsummary_create'),
    path('door_summary', doorsummary_show_view, name='ref_doorsummary'),
    path('door_summary_update/<int:pk>', DoorSummaryUpdateView.as_view(), name='ref_doorsummary_update'),
    path('door_summary_delete/<int:pk>', doorsummary_delete_view, name='ref_doorsummary_delete'),
    # свойста
    # фурнитура
]
