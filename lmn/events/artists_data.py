from .load_events_url import load_URL
from ..models import Artist
from django.http import HttpResponse

# Get a list of artists
def get_artist_data():
    try:
        soup = load_URL()

        # Get artists data and add them to the artist_list
        artists = soup.find_all('h2', {'class' : 'event-5daafce9'})
        for artist in artists:
            name = artist.text
            Artist(name=name).save()
        
        # return HttpResponse('worked') 
        # This isn't web app code, return a regular python object. 
        # Decide how this function will report success and failure to the caller.

    except Exception as e:
        print(e)