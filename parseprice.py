def parsePrice(price):
    #just removes all the symbols 
    price = price.replace(".", "")
    price = price.replace("$", "")
    price = price.replace(",", "")

    finalPrice = int(price)
    #return
    return finalPrice