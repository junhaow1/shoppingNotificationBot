import requests
from bs4 import BeautifulSoup

URL = 'https://www.dell.com/en-au/shop/ultrasharp-27-4k-usb-c-monitor-u2720q/apd/210-auzu/monitors-monitor-accessories'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div',class_ = 'ps-dell-price')
# print(results.prettify())
print(results.text.strip())


URL2 = 'https://www.umart.com.au/Dell-UltraSharp-27-4K-USB-C-Monitor--U2720Q_54620G.html'
page2 = requests.get(URL2)

soup = BeautifulSoup(page2.content, 'html.parser')
# results2 = soup.find_all('div',string = lambda text: 'price' in text.lower() )
results2 = soup.find('div',class_ = 'goods-price')

# print(results2.prettify())
print(results2.text.strip())
