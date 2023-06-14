file = open("new_data.csv", "r")
file.close()
# import pandas as pd

# df = pd.read_csv("new_data.csv")
# # print(df)
# print(df.head(1))
# print(df.tail(2))


# import pandas as pd

# df = pd.read_csv("new_data.csv", index_col="sn")
# # df.iloc[2:4]
# df.loc[4:6]
# print(df)

# iloc loc two keywords

# iloc = index localization


import pandas as pd

df = pd.read_csv("new_data.csv", index_col="Name")
# df.loc['Ram':'Hari']
# df.iloc[3:6]
# print(df)
# print(df['add'] == 'bktpur')

# print(df[df['add'] == 'ktm'])

print(df[(df["add"] == "ktml") & (df["age"] > 34)])
