import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
# import urllib2
import re
import urllib.request  as urllib2 
# from bs4 import BeautifulSoup, Comment
# import requests, re


# google price list

URL = 'https://www.google.com/shopping/product/1465281564801749764?biw=1536&bih=775&sxsrf=ALeKk03V4RUcP81i3R8QN2GZSY0upf-eAg:1610775854414&q=dell+u2720q+australia&oq=dell+u2720q+australia&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMggIABAIEB4QGDIICAAQCBAeEBgyBQgAEM0CUABYAGDII2gAcAB4AIABpwGIAacBkgEDMC4xmAEAqgEPcHJvZHVjdHMtY2Mtd2l6wAEB&sclient=products-cc&uact=5&prds=epd:5377583822449793265,prmr:1&sa=X&ved=0ahUKEwio1o3Y35_uAhVfIbcAHYCTDYwQ3q4ECMEF#online'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find('td',class_ = 'SH30Lb')
# results = soup.find(id = 'sh-oso__online-sellers-grid-wrapper')
# results = soup.find("div")

# results = soup.find("div",class_ = 'QXiyfd')

# print(soup.find_all("div"))


# print(soup.find_all(id="online"))

results=soup.find_all(id="online")

# results2=soup.find_all("table")
results2=soup.find_all(id="sh-osd__online-sellers-grid")



print(results2)



# print(soup.find('section',class_="sBPZEd wcNqgc"))


# print(soup.find(id="sh-osd__online-sellers-cont"))

# print(soup.find_all("td"))



# print(soup.prettify())

# print(soup.get_text())

# print(results.prettify())



# print(results)
# print(results.text)



# comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# tables = []
# for each in comments:
#     if 'table' in each:
#         try:
#             tables.append(pd.read_html(each)[0])
#         except:
#             continue


# print(tables[1])



# comm = re.compile("<!--|-->")
# def make_soup(url):
#     page = urllib2.urlopen(url)
#     soupdata = BeautifulSoup(comm.sub("", page.read()), 'lxml')
#     return soupdata




# page1 = urllib2.urlopen(URL)
# soupdata = BeautifulSoup(comm.sub("", page1.read().decode("utf-8")), 'lxml')

# tableStats = soupdata.find('table', {'id':'sh-osd__online-sellers-grid'})

# print(tableStats)




# def get_player_totals():
#     soup = make_soup("http://www.pro-football-reference.com/years/2015/")

#     tableStats = soup.find('table', {'id':'team_stats'})

#     return tableStats

# print get_player_totals()




# def make_soup(url):
#     r = requests.get(url)
#     soupdata = BeautifulSoup(r.text, 'lxml')
#     return soupdata

# soup = make_soup("http://www.pro-football-reference.com/years/2015/")

# # get the comments
# comments = soup.findAll(text=lambda text:isinstance(text, Comment))

# # look for table with the id "team_stats"
# rx = re.compile(r'<table.+?id="AFC".+?>[\s\S]+?</table>')
# for comment in comments:
#     try:
#         table = rx.search(comment.string).group(0)
#         print(table)
#         # break the loop if found
#         break
#     except:
#         pass