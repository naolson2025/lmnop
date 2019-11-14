import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from .models import Artist, Venue, Show

# Web scrapping from bandsintown website
def loadURL():
    try:
        # Bandsintown url
        url = 'https://www.bandsintown.com/en?came_from=257&sort_by_filter=Number+of+RSVPs'

        # Parsing HTML using BeautifulSoup
        response = requests.get(url)
        get_soup = BeautifulSoup(response.text, "html.parser")

        return get_soup
    except Exception as e:
        print(e)

# Get a list of artists
def getArtistData():
    try:
        # Create artist list
        artist_list = []

        soup = loadURL()

        # Get artists data and add them to the artist_list
        artists = soup.find_all('h2', {'class' : 'event-5daafce9'})
        for artist in artists:
            name = artist.text
            artist_data = Artist(name)
            artist_list.append(artist_data)
            print(artist_data)
        
        return artist_list

    except Exception as e:
        print(e)

def getVenueData():
    try:
        # Create venue list
        venue_list = []

        soup = loadURL()

        # Get venues data and add them to the venue_list
        venue_tag = soup.find_all('div', {'class' : 'event-6891d84c'})
        city_state_tag = soup.find_all('div', {'class' : 'event-c5863c62'})
    
        for venue in venue_tag:
            name = venue.text
            for cities_states in city_state_tag:
                city_ = cities_states.find_all('div')
                city = city_[1].text
                state = city_[1].text
                venue_data = Venue(name, city, state)
                venue_list.append(venue_data)
                print(venue_data)
        
        return venue_list

    except Exception as e:
        print(e)


def getShowData():
    try:
        # Create show list
        show_list = []

        soup = loadURL()

        # Get date, artist, and venue data and add them to the show_list
        date_tag = soup.find_all('div', {'class' : 'event-b58f7990'})
        for date_ in date_tag:
            date = date_.find_all('div')
            month_count = date[0].text
            date_count = date[1].text
            show_date = month_count + date_count
            artist = getArtistData()
            venue = getVenueData
            show_data = Show(show_date, artist, venue)
            show_list.append(show_data)
            print(show_data)
        
        return show_list

    except Exception as e:
        print(e)
    
    