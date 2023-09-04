import requests
from bs4 import BeautifulSoup
import re

search_term = input("Enter search_term name: ")

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4814"
page = requests.get(url).text
doc = BeautifulSoup(page,"html.parser")


page_text = doc.find(class_="list-tool-pagination").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(pages):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4814&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page,"html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(string=re.compile(search_term))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            prices = next_parent.find(class_="price-current").strong.string

            items_found[item] = {"price": int(prices.replace(",","")),"link":link}
        except:
            pass

sorted_items = sorted(items_found.items(),key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])



        
