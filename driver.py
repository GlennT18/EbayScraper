###this file is redundant. Only use this for manual testing ###

from getSite import *
from prices import *
from parseprice import *

#pip install beautiful soup, nicegui, requests

def run(link, price):
    #turn this into parser function, return int and string
    price = int(price)
    link = str(link)

    #call these in go() in main
    links = getSiteContents(link)
    
    #getPrices goes through the list of links
    #and only returns the links that are under the value of
    #the parameter
    links = getInfo(links, price)
    for link in links:
        print(link)

#if __name__ == '__main__':
#    userInputURL = input("Enter Ebay link here:\n")
#    userInputPrice = input("\nEnter price here ($10.00 = 1000)\n")
#
#    price = int(userInputPrice)
#    link = str(userInputURL)
#
#    links = getSiteContents(link)
#
#    links = getPrices(links, price)
#    for link in links:
#        print(link)