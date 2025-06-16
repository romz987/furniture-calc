from django.shortcuts import render


def wardrobe(request):
    context = {
        'title': 'calculator',
    }
    return render(request, 'wardrobe.html', context=context)
