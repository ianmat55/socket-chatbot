import requests
from bs4 import BeautifulSoup

url = 'https//finance.yahoo.com/gainers'

r = requests.get(url)

print(r.status_code) 