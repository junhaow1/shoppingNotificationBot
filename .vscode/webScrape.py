import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')
# print(soup.findAll('a'))

one_a_tag = soup.findAll('a')[38]
link = one_a_tag['href']

download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])

