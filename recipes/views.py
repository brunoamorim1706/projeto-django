from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME')


def contato(request):
    return HttpResponse('CONTATO')


def sobre(resquest):
    return HttpResponse('SOBRE')