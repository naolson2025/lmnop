import requests
import urllib.request

# Web scrapping from bandsintown website
# https://www.dataquest.io/blog/web-scraping-beautifulsoup/
def load_URL():
    try:
        # Bandsintown url
        url = 'https://www.bandsintown.com/en?place_id=ChIJvbt3k5Azs1IRB-56L4TJn5M'

        # Parsing HTML using BeautifulSoup
        response = requests.get(url)
        
        return response
    except Exception as e:
        print(e)

