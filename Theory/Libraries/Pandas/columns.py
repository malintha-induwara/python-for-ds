import pandas as pd 

df = pd.DataFrame({'A':[1,2], 'B':[3,4]})

print(df.columns)
print('\n')
print(list(df.columns))
print('\n')

array = df.values

print(array)
print(type(array))

