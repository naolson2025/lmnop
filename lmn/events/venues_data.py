from .load_events_url import load_URL
from ..models import Venue
from django.http import HttpResponse

def get_venue_data():
    try:
        soup = load_URL()

        # Get venues data and add them to the venue_list
        venue_tag = soup.find_all('div', {'class' : 'event-6891d84c'})
        city_state_tag = soup.find_all('div', {'class' : 'event-c5863c62'})
    
        for venue in venue_tag:
            name = venue.text
            for city_state in city_state_tag:
                city = city_state.text
                state = city_state.text
                Venue(name=name, city=city, state=state).save()
        
        return HttpResponse('worked')

    except Exception as e:
        print(e)