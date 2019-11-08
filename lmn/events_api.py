import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://first-avenue.com/calendar'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

container = soup.find_all('a')
                               
for lines in container:
    title = lines.title
    print(title)

    
    