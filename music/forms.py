""" forms """

from django import forms
from .models import Artist
from django.contrib.auth.models import User


class CreateArtistForm(forms.ModelForm):
    """create artist form"""
    name = forms.CharField()
    image = forms.FileField(required=False)

    class Meta:
        model = Artist
        fields = ("name", "image")
