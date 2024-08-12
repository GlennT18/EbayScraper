from bs4 import BeautifulSoup
import requests
import re

def getInfo(links, value):
    '''
    A little weird, but the value of 5000 is equal to 50.00
    This solution allows us to strip everything from the pricetag that is set on ebay
    and compare it to the value that is passed into the function
    1000 = $10.00
    10000 = $100.00
    100000 = $1,000.00

    '''
    prices = []
    urls = []
    titles = []
    imgs = []
    listOfLists = [prices, urls, titles, imgs]
    for url in links:
        req = requests.get(str(url))
        soup = BeautifulSoup(req.content, "html.parser")

        #parse the soup for the price (span ux-textspans or div x-price-primary)
        price = soup.find('div', {'class': 'x-price-primary'})
        displayPrice = price.text
        conditionalPrice = price.text

        #remove everything other than ints from conditionalPrice
        conditionalPrice = re.sub("[^0-9]", "", conditionalPrice)
        print(conditionalPrice)

        #add logic to compare price to value
        #add to list or ignore
        if(int(conditionalPrice) <= value):
            urls.append(url)
            #add title
            name = soup.find('span', {'class': 'ux-textspans ux-textspans--BOLD'})
            titles.append(name.text)

            #add price
            prices.append(displayPrice)

            #find img(monday)
            imgTag = soup.find('img')
            imgSrc = imgTag['src']
            imgs.append(imgSrc)

            '''
            check for ebaystatic.com
            not sure what that domain is, but it is causing issues
            with images. The links still directed users to the ebay
            page, but when I was researching the domain I did not find
            anything very concrete. 

            Saw a lot of user discussion saying that Ebay was not able
            to help them with the issue, they weren't sure what it was,
            and some users reported that they were stuck on a blank
            screen when they reached the domain. 
            
            When I attempted to reach the domain, I got a network error.
            It is very possible it is something Ebay was using for their 
            backend and it got phased out or never fully actualized. Either
            way I am playing it safe and
            removing any links related to that domain in the meantime
            '''
            if("ebaystatic.com" in imgSrc):
                urls.pop()
                prices.pop()
                titles.pop()
                imgs.pop()


    #return list of lists
    listOfLists.append(prices)
    listOfLists.append(urls)
    listOfLists.append(titles)
    listOfLists.append(imgs)
    return listOfLists