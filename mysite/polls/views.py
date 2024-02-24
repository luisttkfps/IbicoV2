from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo. Você está no Index")# Create your views here.

