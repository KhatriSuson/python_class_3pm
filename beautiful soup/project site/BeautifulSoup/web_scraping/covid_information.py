from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')

app = requests.get(url)
app = BeautifulSoup(app.text, "lxml")
# print(app)



table_code = app.table
# print(table_code)

# body_code = app.body
# print(body_code)

tags = table_code.find_all('tr')
# print(tags)

# for tag in tags:
    # print(tag.text)

data = []
for tag in tags:
    data.append(tag.text.split('\n'))
    # print(data)
    # print(type(data))


data = []
for tag in tags:
    x = tag.text.split('\n')
    if x[1] != "":
        data.append(x[1:])

    # print(data)



import csv
file = open('covid_total_data.csv', 'w')
x = csv.writer(file)
x.writerows(data)
file.close()

import pandas as pd
df = pd.read_csv('covid_total_data.csv', encoding = 'latin1')
# print(df)


Country = list(df['Country,Other'])
Total_Cases = list(df['TotalCases'])
Total_Cases = list(map(lambda x:int(x.replace(',', '')), Total_Cases))

# print(Total_Cases)

# import plotly.graph_objects as go
# fig = go.Figure([go.Bar(x=Country, y=Total_Cases)])
# fig.show()
#
Country = list(df['Country,Other'])[0:5]
Total_Cases = list(df['TotalCases'])
Total_Cases = list(map(lambda x:int(x.replace(',' , '')), Total_Cases))
TotalRecovered = list(df['TotalRecovered'])[0:5]
TotalRecovered = list(map(lambda x:int(x.replace(',', '')),TotalRecovered))

import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(name='Total_Cases', x=Country, y=Total_Cases),
    go.Bar(name='TotalRecovered', x=Country, y=TotalRecovered),
    go.Bar(name='Total_Cases', x=Country, y=Total_Cases)
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()