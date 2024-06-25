from django.shortcuts import render

from goods.models import Products


def catalogue(request):

    goods = Products.objects.all()

    context = {
        'title': 'Home - Catalogue',
        'goods': goods,
    }
    return render(request, 'goods/catalogue.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context ={
        'product': product,
    }

    return render(request, 'goods/product.html', context=context)
