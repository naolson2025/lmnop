from .load_events_url import load_URL
from .venues_data import get_venue_data
from .artists_data import get_artist_data 
from ..models import Show
from django.http import HttpResponse

def get_show_data():
    try:
        show_list = []

        response = load_URL()

        if response is not None:
            soup = BeautifulSoup(response.text, "html.parser")
        
            # Get date, artist, and venue data and add them to the show_list
            date_tag = soup.find_all('div', {'class' : 'event-b58f7990'})
            for date in date_tag:
                if date not in show_list:
                    show_date = date.text
                    artist = get_artist_data()
                    venue = get_venue_data()
                    show_list.append(show_date, artist, venue)
                    Show(show_date=show_date, artist=artist, venue=venue).save()

            return show_list
        else:
            raise Exception('Error retrieving contents')

    except Exception as e:
        print(e)