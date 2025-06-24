from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from furniture.models import Furniture 


class IndexView(LoginRequiredMixin, View):
    template = 'furniture/index.html'

    calc_urls = {
        'шкаф': 'wardrobe:calculator',
        'кухня': 'wardrobe:calculator',
        'комод': 'wardrobe:calculator'
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
