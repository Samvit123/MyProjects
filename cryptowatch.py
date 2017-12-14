#This program lets you find the current value of any major crypotcurrency simply by typing in the name of it
from bs4 import BeautifulSoup
import requests

names = []
prices = []

url = "https://www.worldcoinindex.com/"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')


def restart():
    re = raw_input("Would you like to see the price of another cryptocurrency? 'y/n': ").lower()
    if re == "y":
        currencyfinder()
    elif re == "n":
        print "Thanks for using our cryptocurrency market. Bye"
        exit()


def currencyfinder():
    name_box = soup.find_all('h1')
    price_box = soup.find_all("td", attrs={"class": "number pricekoers lastprice"})

    for i in name_box:
        i = i.text.strip()
        names.append((str(i).title()))

    for p in price_box:
        p = p.text.strip()
        prices.append(str(p))

    global currencies
    currencies = dict(zip(names, prices))

    ask = raw_input("Which cryptocurrency would you like to see the price of? Enter full name of cryptocurrency or "
                    "enter '1' to show a list of all cryptocurrencies and their prices: ").title()

    if ask in currencies:
        print "The current price of " + ask + " is: ", currencies[ask]
        restart()
    elif ask=="1":
        print currencies
        restart()
    else:
        print "Sorry. That is not a recognized cryptocurrency. Please try again."
        restart()


print "Welcome to our live cryptocurrency market."
print "Here you can get the latest prices of all major cryptocurrencies in USD"
currencyfinder()
