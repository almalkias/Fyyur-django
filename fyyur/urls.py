from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('venues/create/', views.create_venue_form, name='create_venue_form')
]
