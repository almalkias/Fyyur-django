from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venues/create/', views.create_venue_form, name='create_venue_form'),
    path('artists/create/', views.create_artist_form, name='create_artist_form'),
    path('artists/', views.artists, name='artists'),
    path('artists/<int:artist_id>', views.show_artist, name='show_artist'),
    path('artists/<int:artist_id>/edit/', views.edit_artist, name='edit_artist'),
]