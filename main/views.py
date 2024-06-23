from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page Home Store',
        'list': ['first', 'second', 'third'],
        'dict': {'first': 1, 'second': 2, 'third': 3},
        'bool': True,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")
