from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name' : 'Bruno Amorim',
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(resquest):
    return HttpResponse('SOBRE')