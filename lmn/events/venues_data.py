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
                venue_list.append(name)
                for city_state in city_state_tag:
                    city_state_string = city_state.text
                    city = city_state_string.split(',', 1)[0]
                    state = city_state_string.split(',', 2)[1]
                    venue_list.append(city)
                    venue_list.append(state)
                    Venue(name=name, city=city, state=state).save()
        
        
            return venue_list
        else:
            raise Exception('Error retrieving contents')
            
    except Exception as e:
        print(e)