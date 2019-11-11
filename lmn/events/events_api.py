import requests
import os

def getEventAPI():
    try:
        # Create the environment variable and import the event key
        event_key = os.environ.get('TicketMaster_KEY')

        # Fetch the data from ticketmaster API
        # Filter the data by dmaID no 336 which targeting the events around minneapolis-saint paul area
        # and by music genre type of events
        url = 'https://app.ticketmaster.com/discovery/v2/events.json?'
        params = {'dmaId' : '336', 'classificationName' : 'music', 'apikey' : event_key}
        data = requests.get(url, params=params).json()
        return data['_embedded']['events']
    except Exception as e:
        print(e)

def getEventData():
    try:
        show_list = []
        venue_list = []

        events = getEventAPI()
        
        for data in events:
            show = data['name']
            venue = data['_embedded']['venues'][0]['name']
            show_list.append(show)
            venue_list.append(venue)
        
        return show_list, venue_list
    
    except Exception as e:
        print(e)
    
    