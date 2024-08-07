from json.tool import main
from unittest import result
from nicegui import ui
from driver import *

#ui practice
ui.html('Welcome to <strong>Ebay Scrapper</strong>')
linkInput = ui.input('Enter Link:')
priceInput = ui.input("Enter desired price($10.00 = 1000):")

ui.button('Run Search', on_click= lambda: go())

ui.run()

def go():
    run(linkInput.value, priceInput.value)