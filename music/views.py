# Django
from django.shortcuts import render
from django.views import View

# Modelos
from .models import Song, Artist

# Create your views here.

# Function-based views.


def index(request):
    """Music index"""
    template = "music/index.html"
    return render(request, template)


def top_songs(request):
    """Top songs"""
    template = "music/top_songs.html"
    return render(request, template)


# Class-based views.


class Index(View):
    """Music index"""

    template = "music/index.html"

    def get(self, request):
        """GET method."""
        return render(request, self.template)


class TopSongs(View):
    """Top songs"""

    template = "music/top_songs.html"

    def get(self, request):
        """GET method."""
        songs = Song.objects.all()

        context = {"songs": songs}
        return render(request, self.template, context)
