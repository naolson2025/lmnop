from load_events_url import load_URL
from .models import Artist
from django.http import HttpResponse

# Get a list of artists
def get_artist_data():
    try:
        artist_list = []

        soup = load_URL()

        # Get artists data and add them to the artist_list
        artists = soup.find_all('h2', {'class' : 'event-5daafce9'})
        for artist in artists:
            name = artist.text
            artist_data.append(name)
            Artist(name=name).save()
        
        return artist_list

    except Exception as e:
        print(e)