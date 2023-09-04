import requests
from bs4 import BeautifulSoup
import json

url = "http://ebravo.pk/classic/softwares"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")

#print(doc)
prices = {}
for page in range(1,10):
    url = f"http://ebravo.pk/classic/softwares?page={page}"
    result = requests.get(url).text
    doc = BeautifulSoup(result,"html.parser")
    tname = doc.find_all(class_="category text-rose")
    tdata=doc.find_all(class_="infohd")
    tviewed = tdata[0]
    tadded = tdata[1]
    tdownloaded=tdata[2]
    for i in range(len(tname)):
        name = tname[i].string
        added = tadded.string
        viewed = tviewed.string
        downloaded = tdownloaded.string
        prices[name] = [added,viewed,downloaded]
        print(name,added,viewed,downloaded)



with open("data2.json","w") as file:
    json.dump(prices,file,indent=3,sort_keys=True)
