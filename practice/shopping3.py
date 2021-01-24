
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

google_url = 'https://www.google.com/shopping/product/1465281564801749764?biw=1536&bih=775&sxsrf=ALeKk03V4RUcP81i3R8QN2GZSY0upf-eAg:1610775854414&q=dell+u2720q+australia&oq=dell+u2720q+australia&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMggIABAIEB4QGDIICAAQCBAeEBgyBQgAEM0CUABYAGDII2gAcAB4AIABpwGIAacBkgEDMC4xmAEAqgEPcHJvZHVjdHMtY2Mtd2l6wAEB&sclient=products-cc&uact=5&prds=epd:5377583822449793265,prmr:1&sa=X&ved=0ahUKEwio1o3Y35_uAhVfIbcAHYCTDYwQ3q4ECMEF#online'
URL = 'https://www.getprice.com.au/dell-ultrasharp-u2720q-27inch-led-monitor.htm'
# url = 'https://www.getprice.com.au/dell-ultrasharp-u2720q-27inch-led-monitor.htm'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div',class_ = 'product_price')

results2 = soup.find("ul",{"class":"product_item_list results"})
print(soup.find("div",{"class":"product_item"}))
# print(results.prettify())
# print(results.text)
print(results2)



# page = urlopen(url)
# html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern,soup,re.IGNORECASE)
title = match_results.group()
# title = re.sub("<.*?>","",title)

print(title)