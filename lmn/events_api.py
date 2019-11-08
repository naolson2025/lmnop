import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://first-avenue.com/calendar'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

one_a_tag = soup.findAll('a')
link = one_a_tag['href']
download_url = 'https://first-avenue.com/calendar' + link
urllib.request.urlretrieve(download_url)
