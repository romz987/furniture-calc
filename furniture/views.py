from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from furniture.models import Furniture 


# Главная страница
class IndexView(LoginRequiredMixin, View):
    template_name = 'furniture/index.html'
    calc_urls = {
        'шкаф': 'wardrobe:calculator',
        'кухня': 'furniture:kitchen_calc_plug',
        'комод': 'furniture:dresser_calc_plug'
    }

    def get(self, request):
        objects = Furniture.objects.all()
        # Добавлеяем url в каждый объект из базы
        for obj in objects:
            url_name = self.calc_urls[str(obj.name).lower()]
            obj.calculator_url = (
                reverse(url_name)
            ) 
        context = {'objects_list': objects}
        return render(request, self.template_name, context)


# Инструкция
@login_required
def wardrobe_man_view(request):
    template_name = 'manuals/wardrobe_manual.html'
    return render(request, template_name)


@login_required
def dresser_man_view(request):
    template_name = 'manuals/dresser_manual.html'
    return render(request, template_name)


@login_required
def kitchen_man_view(request):
    template_name = 'manuals/kitchen_manual.html'
    return render(request, template_name)



# Дополнительно
# заглушки для калькуляторов
@login_required
def dresser_calc_plug_view(request):
    template_name = 'calc_plugs/calc_plug.html'
    context = {
        'title': 'Расчет стоимости комода',
        'in_text': 'калькулятор для комода',
    }
    return render(request, template_name, context=context)


@login_required
def kitchen_calc_plug_view(request):
    template_name = 'calc_plugs/calc_plug.html'
    context = {
        'title': 'Расчет стоимости кухни',
        'in_text': 'калькулятор для кухни',
    }
    return render(request, template_name, context=context)


# заглушки для заказов
@login_required
def dresser_orders_plug_view(request):
    template_name = 'orders_plugs/order_plug.html'
    context = {
        'title': 'Заказы на комод',
    }
    return render(request, template_name, context=context)


@login_required
def kitchen_orders_plug_view(request):
    template_name = 'orders_plugs/order_plug.html'
    context = {
        'title': 'Заказы на кухни',
    }
    return render(request, template_name, context=context)


# заглушки для отмененных заказов
@login_required
def dresser_deactivated_plug_view(request):
    if not request.user.is_superuser:
        raise Http404
    template_name = 'orders_plugs/order_plug.html'
    context = {
        'title': 'Отмененные заказы на комод',
    }
    return render(request, template_name, context=context)


@login_required
def kitchen_deactivated_plug_view(request):
    if not request.user.is_superuser:
        raise Http404
    template_name = 'orders_plugs/order_plug.html'
    context = {
        'title': 'Отмененные заказы на кухни',
    }
    return render(request, template_name, context=context)
