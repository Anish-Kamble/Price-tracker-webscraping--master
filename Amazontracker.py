import requests
from bs4 import BeautifulSoup
import time

import smtplib
prices_list =[]

def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()


def find_price():
    URL = input(" Enter the url:: ")
    r = requests.get(URL,headers={"User-Agent":"Defined"})
    soup = BeautifulSoup(r.content,"html.parser")
    
    try:
        if 'amazon' in URL:
            try:
                prices = soup.find(id="priceblock_dealprice").get_text()
                prices = float(prices.replace(",", "").replace("₹", ""))
                prices_list.append(prices)
            except:
                price_two = soup.find(id = "priceblock_ourprice").get_text()
                prices = float(prices.replace(",", "").replace("₹", ""))
                prices_list.append(prices)
            return prices
        elif 'flipkart' in URL:
            prices = soup.find(class_ = '_1vC4OE _3qQ9m1').get_text()
            prices = float(prices.replace(",", "").replace("₹", ""))
            prices_list.append(prices)
            return prices
    except:
        return

def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

count = 1
while True:
    current_price = find_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            send_email(message,"anishkamble0912@gmail.com","Edi@2022","anishkamble0906@gmail.com") 
    time.sleep(43000)
    count += 1