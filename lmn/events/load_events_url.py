import requests
import urllib.request
from bs4 import BeautifulSoup

# Web scrapping from bandsintown website
def load_URL():
    try:
        # Bandsintown url
        url = 'https://www.bandsintown.com/en?came_from=257&sort_by_filter=Number+of+RSVPs'

        # Parsing HTML using BeautifulSoup
        response = requests.get(url)
        get_soup = BeautifulSoup(response.text, "html.parser")

        return get_soup
    except Exception as e:
        print(e)

