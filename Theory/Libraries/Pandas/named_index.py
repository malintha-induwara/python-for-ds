import pandas as pd 

data = { "calories" : [420,380,390],"duration" : [50,40,45]}


df = pd.DataFrame(data,index=["day1","day2","day3"])

print(df)


#print(df.iloc[2])

#print(df.loc['day3','calories'])
#print(df.iloc[2,0])
#print(df.loc['day2'])
#print(df.iloc[2])
#print(df.loc[['day1','day2']])

print('\n')

print(df['calories'])

print('\n')

print(df.shape)

print('\n')

print(df.size)

print('\n')

print(df.dtypes)

