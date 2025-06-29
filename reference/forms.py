from django import forms
from reference.models import BoxSummary, DoorSummary


class UpdateBoxSummaryForm(forms.ModelForm):
    class Meta:
        model = BoxSummary
        fields = ['material_type', 'material_thickness', 'material_color', 'price_per_sqm'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class UpdateDoorSummaryForm(forms.ModelForm):
    class Meta:
        model = DoorSummary
        fields = ['door_type', 'material_type', 'material_thickness', 'material_color', 'price_per_sqm'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
