import pandas as pd 

data = {'Age':[25,10,30],'Salary':[5000,6000,3000]}


df = pd.DataFrame(data)


print(len(df))

print(df.mean())

print('\n')


print(df['Age'].mean())


print('\n')


print(df['Age'].sum())

print('\n')

print(df.sum())
