import requests

url = 'https://app.ticketmaster.com/discovery/v2/venues.json?apikey=8yFkVOfTiN4HSZQNcjNKWhJ1OTlmYWJh'
params = {'statecode' : 'MN', 'type' : 'venue'}
data = requests.get(url, params=params).json()

venue_data = data['_embedded']['venues']

for data in venue_data:
    name = data['name']
    print(f'Venue: {name}')
