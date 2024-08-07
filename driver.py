from getSite import *
from prices import *

if __name__ == "__main__":
    #returns a list of all the linnks on an Ebay site
    links = getSiteContents()
    
    #getPrices goes through the list of links
    #and only returns the links that are under the value of
    #the parameter
    links = getPrices(links, 1000)
    for link in links:
        print(link)
