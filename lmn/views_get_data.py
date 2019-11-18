from .events import shows_data, venues_data, artists_data
from django.http import HttpResponse

def gather_event_data(request):

    try:
        shows_ = shows_data.get_show_data()
        venues_ = venues_data.get_venue_data()
        artists_ = artists_data.get_artist_data()

        if shows_ == 200 and venues_ == 200 and artists_ == 200: 
            return HttpResponse('ok')
        else:
            return HttpResponse('Error occured')

    except Exception as e:
        print(e)
    