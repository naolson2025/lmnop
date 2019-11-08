import requests

url = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey=8yFkVOfTiN4HSZQNcjNKWhJ1OTlmYWJh'
params = {'dmaId' : '336', 'classificationName' : 'music'}
data = requests.get(url, params=params).json()

events_data = data['_embedded']['events']

for data in events_data:
    name = data['name']
    venue_name = data['_embedded']['venues'][0]['name']
    print(f'Event: {name}')
    print(f'Venue: {venue_name} \n')

