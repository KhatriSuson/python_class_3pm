# Select by class
from urllib3 import *
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
html = urlopen("https://pythonscraping.com/pages/warandpeace.html")
# print(html.read())
## To find all element having class
bs = BeautifulSoup(html.read(),"lxml")
redTagList = bs.findAll("span", {"class":"green"})
# print(redTagList)

for tag in redTagList:
    print(tag.get_text())


# Select by Id

textObj = bs.findAll(id="text")
print(textObj)

for obj in textObj:
    print(obj.get_text())