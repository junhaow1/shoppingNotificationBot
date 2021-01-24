import pandas as pd 
import smtplib, ssl
from project import *
from project import linkList
from project import joinedList


data = {'price':joinedList,'link':linkList}
# print (data)
df = pd.DataFrame(data,columns = ['price','link'])


price_lowest = 950.00
price_lowest_link = ""


for index, row in df.iterrows():
    if (  float(row["price"])<400  ):
        if (  float(row["price"])<price_lowest  ):
            price_lowest = float(row["price"])
            price_lowest_link = row["link"]
    # print (row["price"], row["link"])


# data = pd.read_csv("sales.csv", header=None, float_precision='high') 
# data.head()
# print(data)


#test access element by [][]
# print(data[0][1])


# go through each element by row, get the lowest price 
# if the price is below a value, send the value and the link to target email address

# for index, row in data.iterrows():
#     print (row["0"], row["11"])



# below is previous code

# for price in data:
#     # print(price)
#     # price is 0-11
#     if (float(data[price])<850.0):
#         if (float(data[price])<price_lowest):
#             price_lowest = float(data[price])           
#         # print(float(data[price]))


print(price_lowest)
print(price_lowest_link)

password = '1234554321qwer'

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kevinwjh521@gmail.com"
receiver_email = "kevinwjh520@gmail.com"
# password = input("Type your password and press enter:")
message = """\
Subject: {} price dropped!!!

The lowest price is {}
Go to the link immediately to take it back home now!!
{}

This message is sent from Python.""".format(product_name,price_lowest,price_lowest_link)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



