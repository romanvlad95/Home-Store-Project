from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'Home Store - Main',
        'content': 'Home Store',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home Store - About us',
        'content': 'About us',
        'text_on_page': 'Quality is our primary goal'
    }
    return render(request, 'main/about.html', context)
