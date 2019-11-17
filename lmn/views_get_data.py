from .events import shows_data, venues_data, artists_data
from django.http import HttpResponse

def gather_event_data(request):

    # todo return a HTTP 200 response for success, an error response for errors
    if  == 200:
        shows_data.get_show_data()
        venues_data.get_venue_data()
        artists_data.get_artist_data()
    else:
        return HttpResponse('ok')  

