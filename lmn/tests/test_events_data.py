import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.test import TestCase
import unittest

# https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_testing_with_scrapers.htm

class TestEventsData(unittest.TestCase):

    bs = None

    # Setting up the BeautifulSoup to open the url
    def setUpClass():
        url = "https://www.bandsintown.com/en?place_id=ChIJvbt3k5Azs1IRB-56L4TJn5M"
        TestEventsData.bs = BeautifulSoup(urlopen(url), 'html.parser')
    
    # Test if load the data is loading the needed data
    def test_data_exists(self):
        artist_data = TestEventsData.bs.find_all('h2', {'class' : 'artist-data'})
        venue_data = TestEventsData.bs.find_all('div', {'class' : 'venue-data'})
        city_state_data = TestEventsData.bs.find_all('div', {'class' : 'city-and-state-data'})
        date_data = TestEventsData.bs.find_all('div', {'class' : 'date-data'})

        self.assertIsNotNone(artist_data)
        self.assertIsNotNone(venue_data)
        self.assertIsNotNone(city_state_data)
        self.assertIsNotNone(date_data)