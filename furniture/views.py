from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from furniture.models import Furniture 


class IndexView(LoginRequiredMixin, View):
    template = 'furniture/index.html'

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
        return render(request, self.template, context)


@login_required
def wardrobe_man_view(request):
    return render(request, 'manuals/wardrobe_manual.html')


@login_required
def dresser_man_view(request):
    return render(request, 'manuals/dresser_manual.html')


@login_required
def kitchen_man_view(request):
    return render(request, 'manuals/kitchen_manual.html')


# дополнительно
# заглушки для калькуляторов
@login_required
def dresser_calc_plug_view(request):
    context = {
        'title': 'Расчет стоимости комода',
        'in_text': 'калькулятор для комода',
    }
    return render(request, 'calc_plugs/calc_plug.html', context=context)


@login_required
def kitchen_calc_plug_view(request):
    context = {
        'title': 'Расчет стоимости кухни',
        'in_text': 'калькулятор для кухни',
    }
    return render(request, 'calc_plugs/calc_plug.html', context=context)


# заглушки для заказов
@login_required
def dresser_orders_plug_view(request):
    text = 'список заказов на комод'
    context = {
        'title': text.capitalize(),
        'in_text': text,
    }
    return render(request, 'calc_plugs/calc_plug.html', context=context)


@login_required
def kitchen_orders_plug_view(request):
    text = 'список заказов на кухни'
    context = {
        'title': text.capitalize(),
        'in_text': text,
    }
    return render(request, 'calc_plugs/calc_plug.html', context=context)
