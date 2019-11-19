from .load_events_url import load_URL
from ..models import Venue
from django.http import HttpResponse
from bs4 import BeautifulSoup

def get_venue_data():
    try:
        venue_list = []

        response = load_URL()

        if response is not None:
            soup = BeautifulSoup(response.text, "html.parser")

            # Get venues data and add them to the venue_list
            venue_tag = soup.find_all('div', {'class' : 'event-6891d84c'})
            city_state_tag = soup.find_all('div', {'class' : 'event-c5863c62'})
    
            for venue in venue_tag:
                name = venue.text
                for city_state in city_state_tag:
                    if venue not in venue_list and city_state not in venue_list:
                        city = city_state.text
                        state = city_state.text
                        venue_list.append(name, city, state)
                        Venue(name=name, city=city, state=state).save()

            return venue_list
        else:
            raise Exception('Error retrieving contents')
            
    except Exception as e:
        print(e)