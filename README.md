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



![alt text]([http://url/to/img.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7ae9f9a9-6a52-474c-8669-380b038ff8f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220921T102458Z&X-Amz-Expires=86400&X-Amz-Signature=70fab215575a104eb5b8faa5fb198e6e87dc0fe3653dbb5e0b826861605943a4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject))



## Result

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/329ad143-17da-474b-8a7b-0404b8a2d76d/Untitled.png)

received an email including the product price and purchase link
