from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    return HttpResponse("Bienvenido al servicio de Streaming Lotus!")


def top_songs(request):
    context = {}
    return render(request, 'music/index.html', context)
