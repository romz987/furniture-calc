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
    handles_show_view,
    HandlesUpdateView,
    handles_delete_view,
    HandlesCreateView,
    properties_show_view
)

app_name = ReferenceConfig.name


urlpatterns = [
    # box_summary
    path('box-summary-create', BoxSummaryCreateView.as_view(), name='ref_boxsummary_create'),
    path('box-summary/', boxsummary_show_view, name='ref_boxsummary'),
    path('box-summary-update/<int:pk>', BoxSummaryUpdateView.as_view(), name='ref_boxsummary_update'),
    path('box-summary-delete/<int:pk>', boxsummary_delete_view, name='ref_boxsummary_delete'),
    # door_summary
    path('door-summary-create', DoorSummaryCreateView.as_view(), name='ref_doorsummary_create'),
    path('door-summary', doorsummary_show_view, name='ref_doorsummary'),
    path('door-summary-update/<int:pk>', DoorSummaryUpdateView.as_view(), name='ref_doorsummary_update'),
    path('door-summary-delete/<int:pk>', doorsummary_delete_view, name='ref_doorsummary_delete'),
    # fitting
    path('fitting-create', HandlesCreateView.as_view(), name="ref_fitting_create"),
    path('fitting/', handles_show_view, name='ref_fitting'),
    path('fitting-update/<int:pk>', HandlesUpdateView.as_view(), name="ref_fitting_update"),
    path('fitting-delete/<int:pk>', handles_delete_view, name="ref_fitting_delete"),
    # properties
    path('properties/', properties_show_view, name="ref_properties"),
]
