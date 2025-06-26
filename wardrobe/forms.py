from django import forms 
from reference.models import (
    MaterialType, 
    MaterialThickness, 
    MaterialColor, 
    DoorType, 
    DoorHandle
)


class WardrobeForm(forms.Form):
    # Рамеры
    height = forms.CharField(label='высота мм', widget=forms.TextInput(attrs={"class": "form-control"}))
    width = forms.CharField(label='ширина мм', widget=forms.TextInput(attrs={"class": "form-control"}))
    depth = forms.CharField(label='глубина мм', widget=forms.TextInput(attrs={"class": "form-control"}))
    # Короб
    materials = forms.ModelChoiceField(queryset=MaterialType.objects.none(), label="Материал", widget=forms.Select(attrs={"class": "form-control"}))
    box_thicknesses = forms.ModelChoiceField(queryset=MaterialThickness.objects.none(), label="Толщина материала", widget=forms.Select(attrs={"class": "form-control"}))
    box_colors = forms.ModelChoiceField(queryset=MaterialColor.objects.none(), label="Цвет материала", widget=forms.Select(attrs={"class": "form-control"}))
    # Двери
    door_types = forms.ModelChoiceField(queryset=DoorType.objects.all(), label="Тип дверей", widget=forms.Select(attrs={"class": "form-control"}))
    door_thicknesses = forms.ModelChoiceField(queryset=MaterialThickness.objects.none(), label="Толщина дверей", widget=forms.Select(attrs={"class": "form-control"}))
    door_colors = forms.ModelChoiceField(queryset=MaterialColor.objects.none(), label="Цвет дверей", widget=forms.Select(attrs={"class": "form-control"}))
    # Фурнтирута
    handle_name = forms.ModelChoiceField(queryset=DoorHandle.objects.all(), label="Ручки", to_field_name='name', widget=forms.Select(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        box_materials = kwargs.pop('materials')
        box_thicknesses = kwargs.pop('box_thicknesses')
        box_colors = kwargs.pop('box_colors')
        door_thicknesses = kwargs.pop('door_thicknesses')
        door_colors = kwargs.pop('door_colors')
        door_types = kwargs.pop('door_types')
        #
        super().__init__(*args, **kwargs)
        self.fields['materials'].queryset = box_materials
        self.fields['box_thicknesses'].queryset = box_thicknesses
        self.fields['box_colors'].queryset = box_colors
        self.fields['door_thicknesses'].queryset = door_thicknesses
        self.fields['door_colors'].queryset = door_colors
        self.fields['door_types'].queryset = door_types


class SaveOrderForm(forms.Form):
    customer_name = forms.CharField(label='Имя заказчика', widget=forms.TextInput(attrs={"class": "form-control"}))
    customer_surname = forms.CharField(label='Фамилия заказчика', widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.TextInput(attrs={"class": "form-control"}))
