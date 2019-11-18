from .events import shows_data, venues_data, artists_data
from django.http import HttpResponse

def gather_event_data(request):

    try:
        if shows_data.get_show_data() and 
            venues_data.get_venue_data() and
            artists_data.get_artist_data() == 200: 
            
            return HttpResponse('ok')
        else:
            return HttpResponse('Error occured')

    except Exception as e:
        print(e)
    

