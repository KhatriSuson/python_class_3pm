# step 0:

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"

# step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)



# Step 2: Parse the HTML

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)



# Step 3: HTML Tree traversal

# title = soup.title
# print(title)



# Commanly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

# Get the title of th HTML page
title = soup.title

# Get all the paragraphs from the page

paras = soup.find_all('p')
# print(paras)

anchors = soup.find_all('a')
all_links = set()
# print(anchors)

# Get all the links on the page:
# for link in anchors:
#     print(link.get('href'))

for link in anchors:
    if(link != '#'):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        # print(linkText)


# Get first element in the HTML page
# print(soup.find('p'))


# Get class of any element in the HTML page
# print(soup.find('p')['class'])


# Find all the elements with class lead
# print(soup.find_all('p', class_="lead"))


# Get the text from the tags/ soup

# print(soup.find('p').get_text())
# print(soup.get_text())


# 4. Comments

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()


# navbarSupportedContent = soup.find(id='navbarSupportedContent')
# for elem in navbarSupportedContent.children:
#     print(elem)


element = soup.select('.w-full')
print(element)