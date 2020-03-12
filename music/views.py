from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

# Create your views here.


class index(TemplateView):
    template_name = "music/index.html"


class top_songs(TemplateView):
    template_name = "music/top_songs.html"
