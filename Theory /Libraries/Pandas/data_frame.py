import pandas as pd


data = {'Name':['Alice','Bob','Charile','David'],
        'Age':[25,30,35,40]}


df = pd.DataFrame(data)
#We can change the indexing in dataframe if we want

print(df)
print('\n')

print(type(df))
print('\n')

print(df.loc[1,'Name'])
print('\n')

print(df.loc[3])
print('\n')

print(df.loc[[0,3]])
