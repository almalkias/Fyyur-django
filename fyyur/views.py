from django.shortcuts import render, HttpResponse, redirect
from .models import Venue, Artist, Show
from django.contrib import messages
from datetime import datetime, date
# Create your views here.

def index(request):
    return render(request, 'fyyur/pages/home.html')

# -------------------------------------------------------------------------

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
            seeking_talent = True if 'seeking_talent' in request.POST else False
            seeking_description = request.POST['seeking_description']
            phone = int(request.POST['phone'])

            venue = Venue(name=name,
                          city=city,
                          state=state,
                          address=address,
                          facebook_link=facebook_link,
                          image_link=image_link,
                          website=website,
                          seeking_talent=seeking_talent,
                          seeking_description=seeking_description,
                          phone=phone)

            venue.save()
            messages.success(request, 'Venue ' + name + ' was successfully listed!')
            return redirect('index')

        except:
            messages.error(request, 'An error occurred. Venue ' + name + ' could not be listed.')
            return redirect('create_venue_form')

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
            seeking_venue = True if 'seeking_venue' in request.POST else False
            seeking_description = request.POST['seeking_description']
            phone = request.POST['phone']

            artist = Artist(name=name,
                            city=city,
                            state=state,
                            facebook_link=facebook_link,
                            image_link=image_link,
                            website=website,
                            seeking_venue=seeking_venue,
                            seeking_description=seeking_description,
                            phone=phone)

            artist.save()
            messages.success(request, 'Artist ' + name + ' was successfully listed!')
            return redirect('index')

        except:
            messages.error(request, 'An error occurred. Artist ' + name + ' could not be listed.')
            return redirect('create_artist_form')

    else:
        return render(request, 'fyyur/forms/new_artist.html')

# -------------------------------------------------------------------------

def artists(request):
    data = Artist.objects.all()
    context = {'artists': data}
    return render(request, 'fyyur/pages/artists.html', context)


def venues(request):
    data = []
    cities = []
    venues = Venue.objects.all()

    for venue in venues:
        if venue.city not in cities:
            cities.append(venue.city)
            data.append({
                'city': venue.city,
                'state': venue.state,
                'venues_lst': [{
                    'id': venue.id,
                    'name': venue.name
                }]
            })
        else:
            for e in data:
                if e['city'] == venue.city:
                    e['venues_lst'].append({
                        'id': venue.id,
                        'name': venue.name
                    })

    context = {'areas': data}

    return render(request, 'fyyur/pages/venues.html', context)

# -------------------------------------------------------------------------

def show_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    data = {
        "id": artist.id,
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

    for show in Show.objects.filter(artist=artist).all():
        show_time = show.start_time
        current_time = date.today()
        if show_time.date() < current_time:
            data['past_shows'].append({
                "venue_id": show.venue.id,
                "venue_name": show.venue.name,
                "venue_image_link": show.venue.image_link,
                'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S')
            })
            data['past_shows_count'] += 1
        else:
            data['upcoming_shows'].append({
                "venue_id": show.venue.id,
                "venue_name": show.venue.name,
                "venue_image_link": show.venue.image_link,
                'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S')
            })
            data['upcoming_shows_count'] += 1

    context = {'artist': data}
    return render(request, 'fyyur/pages/show_artist.html', context)


def show_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    data = {
        "id": venue.id,
        "name": venue.name,
        # "genres": venue.genres,
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": venue.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [],
        "upcoming_shows": [],
        "past_shows_count": 0,
        "upcoming_shows_count": 0
    }

    for show in Show.objects.filter(venue=venue).all():
        show_time = show.start_time
        current_time = date.today()
        if show_time.date() < current_time:
            data['past_shows'].append({
                "artist_id": show.artist.id,
                "artist_name": show.artist.name,
                "artist_image_link": show.artist.image_link,
                'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S')
            })
            data['past_shows_count'] += 1
        else:
            data['upcoming_shows'].append({
                "artist_id": show.artist.id,
                "artist_name": show.artist.name,
                "artist_image_link": show.artist.image_link,
                'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S')
            })
            data['upcoming_shows_count'] += 1

    context = {'venue': data}
    return render(request, 'fyyur/pages/show_venue.html', context)

# -------------------------------------------------------------------------

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
        artist.seeking_venue = True if 'seeking_venue' in request.POST else False
        artist.seeking_description = request.POST['seeking_description']
        artist.phone = request.POST['phone']

        artist.save()
        return redirect('show_artist', artist_id=artist_id)

    context = {'artist': artist}
    return render(request, 'fyyur/forms/edit_artist.html', context)


def edit_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    
    if request.method == 'POST':
        venue.name = request.POST['name']
        venue.city = request.POST['city']
        venue.state = request.POST['state']
        # genres = request.POST.getlist('genres')
        venue.facebook_link = request.POST['facebook_link']
        venue.image_link = request.POST['image_link']
        venue.website = request.POST['website_link']
        venue.seeking_talent = True if 'seeking_talent' in request.POST else False
        venue.seeking_description = request.POST['seeking_description']
        venue.address = request.POST['address']
        venue.phone = request.POST['phone']

        venue.save()
        return redirect('show_venue', venue_id=venue_id)

    context = {'venue': venue}
    return render(request, 'fyyur/forms/edit_venue.html', context)

# -------------------------------------------------------------------------

def search_venues(request):
    if request.method == 'POST':
        find_venues = Venue.objects.filter(
            name__contains=request.POST.get('search_term', '')).all()

        response = {"count": len(find_venues), "data": []}
        for venue in find_venues:
            response["data"].append({
                "id": venue.id,
                "name": venue.name,
            })

        context = {
            'search_term': request.POST.get('search_term', ''),
            'results': response
        }
        return render(request, 'fyyur/pages/search_venues.html', context)


def search_artists(request):
    if request.method == 'POST':
        find_artists = Artist.objects.filter(
            name__contains=request.POST.get('search_term', '')).all()

        response = {"count": len(find_artists), "data": []}
        for artist in find_artists:
            response["data"].append({
                "id": artist.id,
                "name": artist.name,
            })

        context = {
            'search_term': request.POST.get('search_term', ''),
            'results': response
        }
        return render(request, 'fyyur/pages/search_venues.html', context)

# -------------------------------------------------------------------------

def delete_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    venue.delete()

    return redirect('venues')


def delete_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.delete()

    return redirect('artists')

# -------------------------------------------------------------------------

def create_shows(request):

    if request.method == 'POST':
        artist_id = request.POST['artist_id']
        venue_id = request.POST['venue_id']
        start_time = datetime.strptime(request.POST['start_time'], '%Y-%m-%dT%H:%M')

        venue = Venue.objects.get(id=venue_id)
        artist = Artist.objects.get(id=artist_id)

        if start_time.date() < date.today():
            messages.error(request, 'old date')
            return redirect('create_shows')

        for show in Show.objects.filter(venue=venue).all():
            if show.start_time.date() == start_time.date() and show.venue == venue:
                messages.error(request, 'venue not avaliable in this date')
                return redirect('create_shows')

        for show in Show.objects.filter(artist=artist).all():
            if show.start_time.date() == start_time.date() and show.artist == artist:
                messages.error(request, 'artist not avaliable in this date')
                return redirect('create_shows')

        show = Show(start_time=start_time, artist=artist, venue=venue)
        show.save()
        messages.success(request, 'show created successfully')
        return redirect('index')

    return render(request, 'fyyur/forms/new_show.html')


def shows(request):
    shows = Show.objects.all()
    data=[]
    for show in shows:
        data.append({
            'artist_image_link': show.artist.image_link, 
            'start_time': show.start_time.strftime('%Y-%m-%d %H:%M:%S'), 
            'artist_id': show.artist.id, 
            'artist_name': show.artist.name,
            'venue_id': show.venue.id, 
            'venue_name': show.venue.name
        })

    context = {'shows': data}
    return render(request, 'fyyur/pages/shows.html', context)