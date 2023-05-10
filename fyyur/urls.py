from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venues/create/', views.create_venue_form, name='create_venue_form'),
    path('artists/create/', views.create_artist_form, name='create_artist_form'),
    path('artists/', views.artists, name='artists'),
    path('venues/', views.venues, name='venues'),
    path('artists/<int:artist_id>', views.show_artist, name='show_artist'),
    path('venues/<int:venue_id>', views.show_venue, name='show_venue'),
    path('artists/<int:artist_id>/edit/', views.edit_artist, name='edit_artist'),
    path('venues/<int:venue_id>/edit/', views.edit_venue, name='edit_venue'),
]