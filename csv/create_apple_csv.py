file = open("apple.csv", "r")
file.close()

import pandas as pd

# data = pd.read_csv("apple.csv")
# print(data)

# data = pd.read_csv('apple.csv', index_col= 'name')
# name = data.loc['Sita':'Gita']
# print(name)


# data = pd.read_csv('apple.csv', index_col= 'sn')
# sn = data.iloc[4:6]
# print(sn)

# data = pd.read_csv('apple.csv')
# print(data.tail(3))
# print(data.head(4))

data = pd.read_csv('apple.csv')
# print(data["add"] == "ktm")
print(data['add'] == "ktm")
