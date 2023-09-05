import re
import requests as r
from bs4 import BeautifulSoup

url = r.get('https://finance.yahoo.com/')
page = url.content
text = BeautifulSoup(page, 'html.parser')
info = text.find('div',class_='YDC-Col1-Stack SideSlot-open_D(n)')
info = text.find('div',id = 'market-summary')
info = text.find('div',id = 'market-summary')
a_list = info.find_all('a')
summary = {}
for item in a_list:
    summary[item.get('title')] = item.get('aria-label')

values = info.find_all('fin-streamer')
stock_info = {}
for stock in values:
    data_symbol = stock.get('data-symbol')
    data_field = stock.get('data-field')
    if data_field == 'regularMarketPrice':
        price = stock.get('value')
    elif data_field == 'regularMarketChangePercent':
        change_perc = stock.get('value')
        stock_info[data_symbol] = {'price':price,'change_perc':change_perc}

print(summary)

