from .events import shows_data
from django.http import HttpResponse

def gather_event_data(request):

    shows_data.get_show_data()
    # todo return a HTTP 200 response for success, an error response for errors
    return HttpResponse('ok')