from json.tool import main
from unittest import result
from nicegui import ui
from driver import *
from getSite import *
from info import *

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
    resultLable = ui.label('Results:')
    columns = [
        {'name': 'price', 'label':'Price', 'field': 'priceField', 'align': 'left'},
        {'name': 'title', 'label': 'Name', 'field': 'titleField', 'align': 'left'},
        {'name': 'link', 'label':'Link', 'field': 'linkField', 'align': 'left'},
        {'name': 'img', 'label': 'Image', 'field': 'imgField', 'align': 'center'}
    ]

    table = ui.table(columns=columns, rows=[], row_key='name').classes('w-full no-wrap')
    #to update this to display URL - remove click here and put {{props.value}}
    table.add_slot('body-cell-link', '''
    <q-td :props="props">
        <a :href="props.value">View Item</a>
    </q-td>
    ''')
    table.add_slot('body-cell-img', '''
    <q-td :props="props">
        <img :src="props.value" width="100" height="100" alt="Image"/>
    </q-td>
    ''')

ui.run()

def go():
    #run(linkInput.value, priceInput.value)
    price = parsePrice(str(priceInput.value))
    link = str(linkInput.value)

    links = getSiteContents(link)
    #links has urls, need to get images and prices from getPrices. Return tuple
    finalLists = getInfo(links, price)

    prices = finalLists[0] 
    urls = finalLists[1] 
    titles = finalLists[2]
    imgs = finalLists[3]  
    
    counter = 0
    for x in urls:
        #update this to add images and prices
        table.add_rows({'priceField': prices[counter], 'titleField': titles[counter], 'linkField': x, 'imgField': imgs[counter]})
        counter += 1
    resultLable.set_text('%3d Results:' % (counter))

