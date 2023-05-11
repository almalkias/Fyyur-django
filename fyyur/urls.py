from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venues/create/', views.create_venue_form, name='create_venue_form'),
    path('artists/create/',
         views.create_artist_form,
         name='create_artist_form'),
    path('artists/', views.artists, name='artists'),
    path('venues/', views.venues, name='venues'),
    path('artists/<int:artist_id>', views.show_artist, name='show_artist'),
    path('venues/<int:venue_id>', views.show_venue, name='show_venue'),
    path('artists/<int:artist_id>/edit/',
         views.edit_artist,
         name='edit_artist'),
    path('venues/<int:venue_id>/edit/', views.edit_venue, name='edit_venue'),
    path('venues/search', views.search_venues, name='search_venues'),
    path('artists/search', views.search_artists, name='search_artists'),
    path('venues/<int:venue_id>/delete/', views.delete_venue, name='delete_venue'),
    path('artists/<int:artist_id>/delete/', views.delete_artist, name='delete_artist'),
]