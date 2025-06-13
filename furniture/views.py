from django.shortcuts import render
from furniture.models import Furniture 


def index(request):
    context = {
        'objects_list': Furniture.objects.all()
    }
    return render(request, 'furniture/index.html', context=context)
