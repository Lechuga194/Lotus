from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top_songs/', views.top_songs, name='top_songs'),
]
