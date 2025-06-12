from django.contrib import admin
from reference.models import (
    MaterialType,
    MaterialThickness,
    MaterialColor,
    DoorType,
    DoorHandle,
    BoxSummary,
    DoorSummary
)

admin.site.register(MaterialType)
admin.site.register(MaterialThickness)
admin.site.register(MaterialColor)
admin.site.register(DoorType)
admin.site.register(DoorHandle)
admin.site.register(BoxSummary)
admin.site.register(DoorSummary)
