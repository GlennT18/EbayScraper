from bs4 import BeautifulSoup
import requests


def getSiteContents():
    #setup the soup
    req = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1313&_nkw=scrap+metal&_sacat=0")
    soup = BeautifulSoup(req.content, "html.parser")
    
    #set anchor
    links = soup.find_all("a")

    #gather all the links
    listLinks = []
    for link in links:
        href = link.get("href")
        if ("https://www.ebay.com/itm/" in str(href)):
            listLinks.append(str(href))

    #clean links. We could set this up with a Set, but then it would be unordered. 
    #i would like them to be ordered for the time being so it is easier to debug, 
    #but in the end I want them to be sorted by price so I can switch this to a set
    #and remove this statement
    cleanedLinkList = listLinks[::2]

    return cleanedLinkList
