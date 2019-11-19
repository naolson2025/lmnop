from django.shortcuts import render
from lmn.events.artists_data import get_artist_data
from lmn.events.shows_data import get_show_data
from lmn.events.venues_data import get_venue_data

def homepage(request):
    # This will load all the data when the application starts
    # TODO: This will load duplicate data, need to add some sort of if/else so it only loads data thats not in the db already
    get_artist_data()
    get_show_data()
    get_venue_data()
    return render(request, 'lmn/home.html')
