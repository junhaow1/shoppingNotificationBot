import pandas as pd 
import smtplib, ssl
from project import *

#old version dont use this one


data = pd.read_csv("sales.csv", header=None, float_precision='high') 
data.head()
print(data)


#test access element by [][]
# print(data[0][1])




price_lowest = 950.00

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

password = '1234554321qwer'

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kevinwjh521@gmail.com"
receiver_email = "kevinwjh520@gmail.com"
# password = input("Type your password and press enter:")
message = """\
Subject: Dell U2720Q 4k ips Monitor price dropped!!!

The lowest price is {}
Go to the link immediately to take it back home now!!

This message is sent from Python.""".format(price_lowest)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



