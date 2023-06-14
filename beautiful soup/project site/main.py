from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup = BeautifulSoup(soup.text, "lxml")
print(soup)

table_code = soup.table
print(table_code)

tags = table_code.find_all('tr')
print(tags)


for tag in tags:
    print(tag.text)

data = []
for tag in tags:
    data.append(tag.text)

print(data)
print(type(data))

