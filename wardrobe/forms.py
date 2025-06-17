from django import forms 
from reference.models import (
    MaterialType, 
    MaterialThickness, 
    MaterialColor, 
    DoorType, 
    DoorHandle
)


class WardrobeForm(forms.Form):
    height = forms.CharField(label='Высота мм', widget=forms.TextInput(attrs={"class": "form-control"}))
    width = forms.CharField(label='Ширина мм', widget=forms.TextInput(attrs={"class": "form-control"}))
    depth = forms.CharField(label='Глубина мм', widget=forms.TextInput(attrs={"class": "form-control"}))

    material = forms.ModelChoiceField(queryset=MaterialType.objects.all(), label="Материал", widget=forms.Select(attrs={"class": "form-control"}))
    thickness = forms.ModelChoiceField(queryset=MaterialThickness.objects.all(), label="Толщина материала", widget=forms.Select(attrs={"class": "form-control"}))
    color = forms.ModelChoiceField(queryset=MaterialColor.objects.all(), label="Цвет материала", widget=forms.Select(attrs={"class": "form-control"}))
    door_type = forms.ModelChoiceField(queryset=DoorType.objects.all(), label="Тип дверей", widget=forms.Select(attrs={"class": "form-control"}))
    handle_type = forms.ModelChoiceField(queryset=DoorHandle.objects.all(), label="Ручки", to_field_name='name', widget=forms.Select(attrs={"class": "form-control"}))
