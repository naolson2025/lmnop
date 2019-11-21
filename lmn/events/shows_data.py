from .load_events_url import load_URL
from .venues_data import get_venue_data
from .artists_data import get_artist_data 
from ..models import Show
from django.http import HttpResponse
from bs4 import BeautifulSoup

def get_show_data():
    try:
        show_list = []

        response = load_URL()

        if response is not None:
            soup = BeautifulSoup(response.text, "html.parser")

            article_tag = soup.find_all('div', {'eventList-5e5f25ca'})

            for article in article_tag:

                # Get date, artist, and venue data and add them to the show_list
                date_tag = soup.find_all('div', {'class' : 'event-b58f7990'})
                artists = soup.find_all('h2', {'class' : 'event-5daafce9'})
                venue_tag = soup.find_all('div', {'class' : 'event-6891d84c'})

                for date in date_tag:
                    show_date = date.text
                    show_list.append(show_date)
                
                for artist in artists:
                    artist_data = artist.text
                    show_list.append(artist_data)
                
                for venue in venue_tag:
                    venue_data = venue.text
                    show_list.append(venue_data)
            
            Show(show_date=show_date, artist=artist_data, venue=venue_data).save()
            return show_list
        else:
            raise Exception('Error retrieving contents')

    except Exception as e:
        print(e)