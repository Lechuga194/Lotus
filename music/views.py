# Django
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User

# Modelos
from .models import Song, Artist

# Forms
from music.forms import CreateArtistForm

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


class CreateArtistView(View):
    """Create artist"""

    template = "music/create_artist.html"

    def get(self, request):
        form = CreateArtistForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = CreateArtistForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            image = form.cleaned_data["image"]
            form.save()
            return redirect("/")
        context = {"form": form}
        return render(request, self.template, context)

        """
        def post(self, request):
        form = CreateArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Valid!</h1>")
        context = {"form": form}
        # return render(request, self.template, context)
        print(form.errors)
        return HttpResponse("<h1>No valid!</h1>")
        """
