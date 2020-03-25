from django.urls import path
from . import views

urlpatterns = [
    # Function-based views
    #     path('', views.index, name='home'),
    #     path('top-songs', views.top_songs, name='top-songs'),
    # Class-based views
    path('', views.Index.as_view(), name='home'),
    path('top_songs', views.TopSongs.as_view(), name='top_songs'),
    path('artist/create-artist',
         views.CreateArtistView.as_view(), name='create_artist')
]
