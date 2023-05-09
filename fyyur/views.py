from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .models import Venue, Artist
from django.contrib import messages
# Create your views here.


def index(request):
  return render(request, 'fyyur/pages/home.html')


def create_venue_form(request):
  if request.method == 'POST':
      try:
          name = request.POST['name']
          city = request.POST['city']
          state = request.POST['state']
          address = request.POST['address']
          # genres = request.POST.getlist('genres')
          facebook_link = request.POST['facebook_link']
          image_link = request.POST['image_link']
          website = request.POST['website_link']
          seeking_talent = True if len(
              request.POST.getlist('seeking_talent')) > 0 else False
          seeking_description = request.POST['seeking_description']

          venue = Venue(name=name,
                        city=city,
                        state=state,
                        address=address,
                        facebook_link=facebook_link,
                        image_link=image_link,
                        website=website,
                        seeking_talent=seeking_talent,
                        seeking_description=seeking_description)

          venue.save()
          messages.success(request, 'Venue ' + name + ' was successfully listed!')
          return redirect('index')

      except:
          messages.error(request, 'An error occurred. Venue ' + name + ' could not be listed.')
          return redirect('index')

  else:
      return render(request, 'fyyur/forms/new_venue.html')


def create_artist_form(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            city = request.POST['city']
            state = request.POST['state']
            # genres = request.POST.getlist('genres')
            facebook_link = request.POST['facebook_link']
            image_link = request.POST['image_link']
            website = request.POST['website_link']
            seeking_venue = True if len(
                request.POST.getlist('seeking_venue')) > 0 else False
            seeking_description = request.POST['seeking_description']

            artist = Artist(name=name,
                            city=city,
                            state=state,
                            facebook_link=facebook_link,
                            image_link=image_link,
                            website=website,
                            seeking_venue=seeking_venue,
                            seeking_description=seeking_description)

            artist.save()
            messages.success(request, 'Artist ' + name + ' was successfully listed!')
            return redirect('index')

        except:
            messages.error(request,'An error occurred. Artist ' + name + ' could not be listed.')
            return redirect('index')

    else:
        return render(request, 'fyyur/forms/new_artist.html')


def artists(request):
  data = Artist.objects.all()
  context = {'artists': data}
  return render(request, 'fyyur/pages/artists.html', context)


def show_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    data = {
        "id": artist_id,
        "name": artist.name,
        # "genres": artist.genres,
        "city": artist.city,
        "state": artist.state,
        "phone": artist.phone,
        "website": artist.website,
        "facebook_link": artist.facebook_link,
        "seeking_venue": artist.seeking_venue,
        "seeking_description": artist.seeking_description,
        "image_link": artist.image_link, 
        "past_shows": [],
        "upcoming_shows": [],
        "past_shows_count": 0,
        "upcoming_shows_count": 0
    }

    # for show in artist.shows:
    #     show_time = show.start_time.replace(tzinfo=utc)
    #     current_time = datetime.now().replace(tzinfo=utc)
    #     if show_time < current_time:
    #         data['past_shows'].append({
    #             "venue_id": show.venue_id,
    #             "venue_name": show.venue.name,
    #             "venue_image_link": show.venue.image_link,
    #             'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    #         })
    #         data['past_shows_count'] += 1
    #     else:
    #         data['upcoming_shows'].append({
    #             "venue_id": show.venue_id,
    #             "venue_name": show.venue.name,
    #             "venue_image_link": show.venue.image_link,
    #             'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    #         })
    #         data['upcoming_shows_count'] += 1  

    context = {'artist': artist}
    return render(request, 'fyyur/pages/show_artist.html', context)


def edit_artist(request, artist_id):
  artist = Artist.objects.get(id=artist_id)

  if request.method == 'POST':
    artist.name = request.POST['name']
    artist.city = request.POST['city']
    artist.state = request.POST['state']
    # genres = request.POST.getlist('genres')
    artist.facebook_link = request.POST['facebook_link']
    artist.image_link = request.POST['image_link']
    artist.website = request.POST['website_link']
    artist.seeking_venue = True if len(request.POST.getlist('seeking_venue')) > 0 else False
    artist.seeking_description = request.POST['seeking_description']

    artist.save()
    return redirect('show_artist', artist_id=artist_id)
    
  context = {'artist': artist}

  return render(request, 'fyyur/forms/edit_artist.html', context)
