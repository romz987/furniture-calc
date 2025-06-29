from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from reference.models import (
    BoxSummary,
    DoorSummary,
)
from reference.forms import (
    UpdateBoxSummaryForm,
    UpdateDoorSummaryForm,
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
        return redirect('furniture:index')
    context = {
        'title': 'Вы уверены, что хотите удалить запись?'
    }
    return render(request, 'confirm_delete.html', context=context)


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
        context['title'] = 'Изменить материал короба'
        return context



# Материалы дверей
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
        return redirect('furniture:index')
    context = {
        'title': 'Вы уверены, что хотите удалить запись?'
    }
    return render(request, 'confirm_delete.html', context=context)


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
    template_name = 'box/box_reference_create.html'
    success_url = reverse_lazy('reference:ref_doorsummary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # мой контекст
        context['title'] = 'Добавить материал двери'
        return context
