## What the code does

The shopping notification bot could automatically scrape websites for a specific product, monitors the price and send users an email when the price drops to the user’s budget.  

## How to use

For example I wanna buy an airpods pro. 

I input several parameters to the python function 

`def project(priceNotification, priceBottom, email_address, shopping_url):`

1. priceNotification = 350 
    
    This is my budget price, I’d like to buy under 350 dollars 
    
2. priceBottom = 200
    
    This is a price to filter fake or used/second-hand products
    
3. email_address = kevinwjh520@gmail.com
    
    Just put the receriver email address here
    
4. google shopping URL of the product(as following graph)


[image1.png
](https://github.com/junhaow1/shoppingNotificationBot/blob/main/image1.png?raw=true)

## Result

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/329ad143-17da-474b-8a7b-0404b8a2d76d/Untitled.png)

received an email including the product price and purchase link
