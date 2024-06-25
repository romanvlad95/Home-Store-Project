from django.shortcuts import render

from goods.models import Products


def catalogue(request):

    goods = Products.objects.all()

    context = {
        'title': 'Home - Catalogue',
        'goods': goods,
    }
    return render(request, 'goods/catalogue.html', context)


def product(request):
    return render(request, 'goods/product.html')
