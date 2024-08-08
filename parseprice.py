def parsePrice(price):
    #split on period if there is one
    if("." in price):
        price = price.replace(".", "")
    #remove commas and dollar sign
    if("$" in price):
        price = price.replace("$", "")
    #concatonate both strings
    if("," in price):
        price = price.replace(",", "")

    finalPrice = int(price)
    #return
    return finalPrice