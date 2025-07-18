from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from reference.models import (
    BoxSummary,
    DoorSummary,
    DoorHandle,
    # Свойства
    MaterialType,
    MaterialThickness,
    MaterialColor,
    DoorType,
)
from reference.forms import (
    UpdateBoxSummaryForm,
    UpdateDoorSummaryForm,
    UpdateFittingForm,
)


# Материалы короба
@login_required
def boxsummary_show_view(request):
    objects_list = BoxSummary.objects.all()
    context = {
        'title': 'Материалы короба',
        'objects_list': objects_list
    
    }
    return render(request, 'box/box_reference.html', context=context)


@login_required 
def boxsummary_delete_view(request, pk):
    record = get_object_or_404(BoxSummary, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('reference:ref_boxsummary')
    # Страница подтвержения удаления
    template_name = 'common/confirm_delete.html'
    context = {
        'title': 'Удаление',
        'message': 'Вы уверены, что хотите удалить запись?'
    }
    return render(request, template_name, context=context)


class BoxSummaryUpdateView(LoginRequiredMixin, UpdateView):
    model = BoxSummary 
    form_class = UpdateBoxSummaryForm
    template_name = 'box/box_reference_update.html'
    success_url = reverse_lazy('reference:ref_boxsummary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Изменить материал короба'
        return context


class BoxSummaryCreateView(LoginRequiredMixin, CreateView):
    model = BoxSummary 
    form_class = UpdateBoxSummaryForm
    template_name = 'box/box_reference_create.html'
    success_url = reverse_lazy('reference:ref_boxsummary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Добавить материал короба'
        return context



# Материалы дверей
@login_required
def doorsummary_show_view(request):
    objects_list = DoorSummary.objects.all()
    context = {
        'title': 'Материалы дверей',
        'objects_list': objects_list
    
    }
    return render(request, 'doors/door_reference.html', context=context)


@login_required 
def doorsummary_delete_view(request, pk):
    record = get_object_or_404(DoorSummary, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('reference:ref_doorsummary')
    # Страница подтвержения удаления
    template_name = 'common/confirm_delete.html'
    context = {
        'title': 'Удаление',
        'message': 'Вы уверены, что хотите удалить запись?'
    }
    return render(request, template_name, context=context)


class DoorSummaryUpdateView(LoginRequiredMixin, UpdateView):
    model = DoorSummary 
    form_class = UpdateDoorSummaryForm
    template_name = 'doors/door_reference_update.html'
    success_url = reverse_lazy('reference:ref_doorsummary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Изменить материал двери'
        return context


class DoorSummaryCreateView(LoginRequiredMixin, CreateView):
    model = DoorSummary 
    form_class = UpdateDoorSummaryForm
    template_name = 'doors/door_reference_create.html'
    success_url = reverse_lazy('reference:ref_doorsummary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Добавить материал двери'
        return context


# Фурнитура
@login_required
def handles_show_view(request):
    objects_list = DoorHandle.objects.all()
    context = {
        'title': 'Мебельные ручки',
        'objects_list': objects_list
    
    }
    return render(request, 'fitting/fit_reference.html', context=context)


@login_required 
def handles_delete_view(request, pk):
    record = get_object_or_404(DoorHandle, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('reference:ref_fitting')
    # Страница подтвержения удаления
    template_name = 'common/confirm_delete.html'
    context = {
        'title': 'Удаление',
        'message': 'Вы уверены, что хотите удалить запись?'
    }
    return render(request, template_name, context=context)


class HandlesUpdateView(LoginRequiredMixin, UpdateView):
    model = DoorHandle 
    form_class = UpdateFittingForm
    template_name = 'fitting/fit_reference_update.html'
    success_url = reverse_lazy('reference:ref_fitting')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Изменить мебельную ручку'
        return context


class HandlesCreateView(LoginRequiredMixin, CreateView):
    model = DoorHandle 
    form_class = UpdateFittingForm
    template_name = 'fitting/fit_reference_create.html'
    success_url = reverse_lazy('reference:ref_fitting')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Добавить мебельную ручку'
        return context



# Свойства
@login_required
def properties_show_view(request):
    material_types = MaterialType.objects.all().order_by('id')
    material_thick = MaterialThickness.objects.all().order_by('id')
    material_colors = MaterialColor.objects.all().order_by('id')
    doors = DoorType.objects.all().order_by('id')
    context = {
        'title': 'Свойства',
        'material_types': material_types,
        'material_thick': material_thick,
        'material_colors': material_colors,    
        'doors': doors,
    }
    return render(request, 'properties/pr_reference.html', context=context)
