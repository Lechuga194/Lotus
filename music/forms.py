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

    def clean_name(self):
        data = self.cleaned_data["name"]
        if Artist.objects.filter(name=data).count() > 0:
            raise forms.ValidationError("This name already exists!")
        return data
