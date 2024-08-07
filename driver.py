from getSite import *
from prices import *

if __name__ == "__main__":
    #returns a list of all the linnks on an Ebay site
    userInputURL = input("Enter Ebay link here:\n")
    userInputPrice = input("Enter price here ($10.00 = 1000)\n")
    userInputPrice = int(userInputPrice)
    links = getSiteContents(userInputURL)
    
    #getPrices goes through the list of links
    #and only returns the links that are under the value of
    #the parameter
    links = getPrices(links, userInputPrice)
    for link in links:
        print(link)
