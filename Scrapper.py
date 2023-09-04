import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://coinmarketcap.com/"
result = requests.get(url).text

doc = BeautifulSoup(result,"html.parser")
tprice = doc.find_all(class_="sc-a0353bbc-0 gDrtaY")

tname = doc.find_all(class_="sc-4984dd93-0 kKpPOn")



prices = {}
for i in range(len(tname)):
    name = tname[i].string
    price = tprice[i].string
    prices[name] = price
    

print(prices)

with open("data.json","a") as file:
    json.dump(prices,file,indent=3,sort_keys=True)






"""trs = tbody.contents

name = tbody.
print()

"""

"""for tr in trs[:10]:
    name,price = tr.contents[2:4]
    print(name)
    #fixed_name = name.p.string
    #fixed_price = price.a.string
    #prices[fixed_name] = fixed_price


#print(prices)"""