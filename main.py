from json.tool import main
from unittest import result
from nicegui import ui
from driver import *
from getSite import *
from prices import *

result_label = None

#ui practice
with ui.row().classes('w-full border'):
    ui.space()
    ui.html('Welcome to <strong>Ebay Scrapper</strong>').style('font-size:150%')
    ui.space()

with ui.column().classes('w-full no-wrap'):
    #user input section
    linkInput = ui.input('Enter Link:').classes('w-1/4')
    priceInput = ui.input("Enter desired price(ex. $10.00):").classes('w-1/4')
    ui.button('Run Search', on_click= lambda: go())
    result_label = ui.label('Results will be displayed here').classes('mt-4')

ui.run()

def go():
    global result_label
    #run(linkInput.value, priceInput.value)
    price = int(priceInput.value)
    link = str(linkInput.value)

    links = getSiteContents(link)
    #breaks in getPrices
    links = getPrices(links, price)

    result_text = '\n'.join(str(link) for link in links)  
    result_label.set_text(result_text)  
