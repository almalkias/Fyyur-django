from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
  return render(request, 'fyyur/pages/home.html')

def create_venue_form(request):
  if request.method == 'POST':
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    address = request.POST['address']
    genres = request.POST.getlist('genres')
    facebook_link = request.POST['facebook_link']
    image_link = request.POST['image_link']
    website_link = request.POST['website_link']
    seeking_talent = True if len(request.POST.getlist('seeking_talent')) > 0 else False
    seeking_description = request.POST['seeking_description']

    return redirect('index')



  return render(request, 'fyyur/forms/new_venue.html')