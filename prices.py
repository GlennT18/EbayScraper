from xml.etree.ElementTree import tostring
from bs4 import BeautifulSoup
import requests
import re

def getPrices(links, value):
    '''
    A little weird, but the value of 5000 is equal to 50.00
    This solution allows us to strip everything from the pricetag that is set on ebay
    and compare it to the value that is passed into the function
    1000 = $10.00
    10000 = $100.00
    100000 = $1,000.00

    '''
    withinPriceRangeList = []
    for url in links:
        req = requests.get(str(url))
        soup = BeautifulSoup(req.content, "html.parser")

        #parse the soup for the price (span ux-textspans or div x-price-primary)
        price = soup.find('div', {'class': 'x-price-primary'})
        price = str(price)

        #pull the price out of the div. Wanted to use regex but there are numbers within the div
        #we are just using split function on the $ and ' ' after the number
        #this is disgusting pls fix later
        flag = False
        finalPrice = ""
        for char in price:
            if(char == "$"):
                flag = True
            if(flag and char != "." and char != "$"):
                if(char == "<" or char == "/"):
                    flag = False
                    break
                elif(char == ","):
                    continue
                finalPrice += char
        finalPrice = int(finalPrice)

        #add logic to compare price to value
        #add to list or ignore
        if(finalPrice <= value):
            withinPriceRangeList.append(url)

    #return list
    return withinPriceRangeList