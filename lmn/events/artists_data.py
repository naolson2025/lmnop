from .load_events_url import load_URL
from ..models import Artist
from django.http import HttpResponse
from bs4 import BeautifulSoup

# Get a list of artists
def get_artist_data():
    try:
        artist_list = []

        response = load_URL()

        if response is not None:
            soup = BeautifulSoup(response.text, "html.parser")
            
            article_tag = soup.find_all('div', {'eventList-5e5f25ca'})

            for article in article_tag:

                artists = soup.find_all('h2', {'class' : 'event-5daafce9'})

                # Get artists data and add them to the artist_list
                for artist in artists:
                    if artist not in artist_list:
                        name = artist.text
                        artist_list.append(name)
                        Artist(name=name).save()

            return artist_list
        else:
            raise Exception('Error retrieving contents')
            
    except Exception as e:
        print(e)