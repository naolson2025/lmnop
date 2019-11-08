import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://first-avenue.com/calendar'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.findAll('article')

for article in articles: 
    links = article.find_all(class_ = "even")
    for l in links:
        print(l.text)

""" So you could examine all the l.text strings. 
The first one is the show, unless it ends with 'presents' in which case it's the second one. 
The venue is the l.text that starts with 'at' """



