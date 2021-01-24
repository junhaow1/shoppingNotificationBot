import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import re

import csv




#web scraping source 1 : individual websites 

URL = 'https://www.dell.com/en-au/shop/ultrasharp-27-4k-usb-c-monitor-u2720q/apd/210-auzu/monitors-monitor-accessories'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div',class_ = 'ps-dell-price')
pricelist1 = re.findall("\d+\.\d+", results.text.strip())
print(re.findall("\d+\.\d+", results.text.strip()))

# create a list to save href link to the product
linkList = []

#add first url to the list
linkList.append(URL)


URL2 = 'https://www.umart.com.au/Dell-UltraSharp-27-4K-USB-C-Monitor--U2720Q_54620G.html'
page2 = requests.get(URL2)

soup = BeautifulSoup(page2.content, 'html.parser')
results2 = soup.find('div',class_ = 'goods-price')

pricelist2 = re.findall("\d+\.\d+", results2.text.strip())
print(re.findall("\d+\.\d+", results2.text.strip()))
#add sec url to the list
linkList.append(URL2)

# test
# print(linkList)


#web scraping source 2 : google shopping price list

  
#url of the page we want to scrape 
url="https://www.google.com/shopping/product/6377659988323960368?q=airpods+pro&sxsrf=ALeKk0132Gctf9nmdN05E4aI8iofBWPaeA:1611259968418&biw=1745&bih=881&prds=epd:13421449088386249105,prmr:1&sa=X&ved=0ahUKEwiLpLuR663uAhXN9nMBHVrsC2kQ3q4ECJoE#online"
# url = "https://www.google.com/shopping/product/17116295002256069167?q=philips+air+fryer&sxsrf=ALeKk02xRkUSwF4paxvJHsJO6ZQtRR30zg:1611383913852&biw=1745&bih=881&prds=epd:6863085681753514412,prmr:1&sa=X&ved=0ahUKEwjzyLvvuLHuAhUbyDgGHYHlDmQQ3q4ECM4F#online"
product_name = ""



# initiating the webdriver. Parameter includes the path of the webdriver. 
driver = webdriver.Chrome('./chromedriver')  
driver.get(url)  
  
# this is just to ensure that the page is loaded 
time.sleep(1)  
  
html = driver.page_source 
  
# this renders the JS code and stores all 
# of the information in static HTML code. 
  
# Now, we could simply apply bs4 to html variable 
soup = BeautifulSoup(html, "html.parser") 

product_title = soup.find('span',{'class' : 'BvQan sh-t__title-pdp sh-t__title translate-content'})
print(product_title.text)
product_name = product_title.text
priceTable = soup.find('table', {'id' : 'sh-osd__online-sellers-grid'}) 
priceRow = priceTable.find_all('div', {'class' : 'sh-osd__total-price'}) 

joinedList = pricelist1+pricelist2


#add href to the linkList
urls = priceTable.find_all('a',{'class' :"internal-link ZvnyBe shntl"})
# print(urls)
base_url = 'https://www.google.com'

for eachLink in urls:
    # we need to add base url in front of the link
    linkList.append(base_url+eachLink['href'])


print(linkList)
  
# printing top ten job profiles 
count = 0
for price in priceRow : 
    pricelist3 = re.findall("\d+\.\d+", price.text)
    joinedList += pricelist3

    print(re.findall("\d+\.\d+", price.text))

    # print(price.text) 
    count = count + 1
    if(count == 100) : 
        break
  
driver.close() # closing the webdriver 


print(joinedList)



with open('priceAndUrl.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(joinedList)
    csv_writer.writerow(linkList)





