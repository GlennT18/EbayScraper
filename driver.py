from getSite import *
from prices import *

#pip install beautiful soup, nicegui, requests

def run(link, price):
    #returns a list of all the linnks on an Ebay site
    #userInputURL = input("Enter Ebay link here:\n")
    #userInputPrice = input("\nEnter price here ($10.00 = 1000)\n")
    price = int(price)
    link = str(link)
    links = getSiteContents(link)
    
    #getPrices goes through the list of links
    #and only returns the links that are under the value of
    #the parameter
    links = getPrices(links, price)
    for link in links:
        print(link)