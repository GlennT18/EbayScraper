import re

def parsePrice(price):
    #just removes all the symbols 
    price = re.sub("[^0-9]", "", price)
    finalPrice = int(price)
    #return
    return finalPrice