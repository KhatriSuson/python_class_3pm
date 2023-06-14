# select from class
from urllib3 import *
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
html = urlopen('https://www.facebook.com/?stype=lo&jlou=Afc_SiWt-xJOUmb0RVvH8YmmZ2GAu6h19lLr4-RWRgqnRipH8J7BZV9BymHSr8DmnZmXwp01-1KAaGnXSBvl7AJaXdAyHXPpMLSEeQWhNpqp8A&smuh=30561&lh=Ac8pYkTdudvARa4i_vk')
print(html.read())
bs = BeautifulSoup(html.read(), "lxml")
form_class = bs.findAll("span",{"class":"_4bl7 _9ji4"})
# print(form_class)
for tag in form_class:
    print(form_class.get_text())

