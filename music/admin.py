"""Models in Music admin"""

# Django
from django.contrib import admin

# Register your models here.
# Models

from .models import Song, Artist

admin.site.register(Song)
admin.site.register(Artist)
