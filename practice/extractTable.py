# from bs4 import BeautifulSoup
# import urllib.request  as urllib2 
# # import urllib2 

# import re
# comm = re.compile("<!--|-->")
# def make_soup(url):
#     page = urllib2.urlopen(url)
#     soupdata = BeautifulSoup(comm.sub("", page.read()), 'lxml')
#     return soupdata

#     # https://www.google.com/shopping/product/11559963950601094589?q=dell+u2720q+australia&sxsrf=ALeKk03YfU8bDzL9JoalgdHWaqyStTBuDQ:1610873634120&biw=1920&bih=969&prds=epd:1039039642099595239,prmr:1&sa=X&ved=0ahUKEwjmzfL2y6LuAhXm4nMBHSIWDzIQ3q4ECMAF#online

# def get_player_totals():
#     soup = make_soup("http://www.pro-football-reference.com/years/2015/")

#     tableStats = soup.find('table', {'id':'team_stats'})

#     return tableStats

# print (get_player_totals())

# import urllib.request  as urllib2 

# from urllib2 import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://oil-price.net').read()
# soup = BeautifulSoup(html)

# div = soup.find("div",{"id":"cntPos"})
# table1 = div.find("table",{"class":"cntTb"})
# tb1_body = table1.find("tbody")
# tb1_rows = tb1_body.find_all("tr")
# tb1_row = tb1_rows[1]
# td = tb1_row.find("td",{"class":"cntBoxGreyLnk"})
# print td


import requests
from bs4 import BeautifulSoup

URL = 'https://www.dell.com/en-au/shop/ultrasharp-27-4k-usb-c-monitor-u2720q/apd/210-auzu/monitors-monitor-accessories'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

print(soup.find("title"))
print(soup.find("div"))

print(soup.find("table",{"class":"dOwBOc"}))