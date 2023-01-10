from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Здесь буедт выведен список объявлений.")
# Create your views here.
