import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import csv
import pandas as pd
import smtplib, ssl


# future implement command line input
# priceNotification = float(input())
# priceBottom = float(input())

def project(priceNotification, priceBottom, email_address, shopping_url):
    # section 1
    # web scraping source 1 : individual websites
    # test purpose : in the future prepare for scraping static shopping websites like jb hifi or mwave

    URL = 'https://www.dell.com/en-au/shop/dell-ultrasharp-27-4k-usb-c-hub-monitor-u2723qe/apd/210-bdzq/monitors-monitor-accessories'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='ps-dell-price')
    pricelist1 = re.findall("\d+\.\d+", results.text.strip())
    print(re.findall("\d+\.\d+", results.text.strip()))

    # create a list to save href link (corresponding to each product from different websites)
    linkList = []

    # add first url to the url list
    linkList.append(URL)

    # sec specific static website 
    URL2 = 'https://www.umart.com.au/product/dell-ultrasharp-27-4k-usb-c-monitor-u2720q-54620'
    page2 = requests.get(URL2)
    soup = BeautifulSoup(page2.content, 'html.parser')
    results2 = soup.find('div', class_='goods-price')
    pricelist2 = re.findall("\d+\.\d+", results2.text.strip())
    print(re.findall("\d+\.\d+", results2.text.strip()))
    # add sec url to the url list
    linkList.append(URL2)

    # section 2
    # web scraping source 2 : google shopping price table

    # url of the page we want to scrape
    url = shopping_url
    product_name = ""

    # codes below use selenium to initiate the webdriver. Parameter includes the path of the webdriver. 
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    # this is just to ensure that the page is loaded 
    # wait for one sec
    time.sleep(1)
    html = driver.page_source
    # this renders the JS code and stores all of the information in static HTML code. 

    # Now, we could simply apply bs4 to html variable , like we always do
    soup = BeautifulSoup(html, "html.parser")
    product_title = soup.find('span', {'class': 'BvQan sh-t__title-pdp sh-t__title translate-content'})
    print(product_title.text)
    product_name = product_title.text
    priceTable = soup.find('table', {'id': 'sh-osd__online-sellers-grid'})
    priceRow = priceTable.find_all('div', {'class': 'sh-osd__total-price'})
    joinedList = pricelist1 + pricelist2

    # get/scrape url
    # add href to the url List
    urls = priceTable.find_all('a', {'class': "internal-link ZvnyBe shntl"})
    base_url = 'https://www.google.com'

    # add full url into the url list
    for eachLink in urls:
        # we need to add base url in front of each link
        linkList.append(base_url + eachLink['href'])

    print(linkList)

    # add each price in the google shopping table into price list
    count = 0
    for price in priceRow:
        pricelist3 = re.findall("\d+\.\d+", price.text)
        joinedList += pricelist3
        print(re.findall("\d+\.\d+", price.text))

        count = count + 1
        if (count == 100):
            break

    driver.close()  # closing the webdriver
    print(joinedList)

    # write price and url lists to csv file
    with open('priceAndUrl.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(joinedList)
        csv_writer.writerow(linkList)

    # put data(price and url list) into files we can process

    # create a new pandas.df file . in columns , column name: price , link (url)
    data = {'price': joinedList, 'link': linkList}
    df = pd.DataFrame(data, columns=['price', 'link'])
    # set a starting original price 
    price_lowest = 100000.00
    price_lowest_link = ""
    # input
    price_expectation = priceNotification
    price_bottom = priceBottom

    # simple algorithm: find cheapest one under our expectation price and above the bottom-price(avoid fake goods)
    # iterate df rows to find the lowest price under our input parameter(threshold)
    for index, row in df.iterrows():
        if (float(row["price"]) < price_expectation):
            if ((float(row["price"]) < price_lowest) & (float(row["price"]) > price_bottom)):
                price_lowest = float(row["price"])
                price_lowest_link = row["link"]

    # test if we get the price and url
    print(price_lowest)
    print(price_lowest_link)

    # section 3 : send email by SMTP

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "kevinwjh521@gmail.com"
    # input parameter
    receiver_email = email_address
    # receiver_email = "shouyinzuo@gmail.com"

    # password = input("Type your password and press enter:")
    password = '1234554321qwer'

    # below is plain text email message
    message = """\
    Subject: {} price dropped!!!

    The lowest price is {}
    Go to the link immediately to take it back home now!!
    {}

    This message is sent from Python.""".format(product_name, price_lowest, price_lowest_link)

    # smtp protocol to send mails through gmail server
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# run the project file
project(350, 250, "kevinwjh520@gmail.com",
        "https://www.google.com/shopping/product/8300897844992207877/offers?q=airpods+pro&sxsrf=ALiCzsY0ht2PJUyebSBhgg2y9ERuw4feGg:1663642049364&biw=1728&bih=1001&dpr=2&prds=eto:2754270653443076419_0,pid:3006283522005438348,rsk:PC_7827190084446473420&sa=X&ved=0ahUKEwjYgfbLraL6AhUp8zgGHdWhA0cQ3q4ECPUL")
