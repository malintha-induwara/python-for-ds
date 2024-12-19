import pandas as pd


data = {'A':[1,2],'B':[3,4]}

df = pd.DataFrame(data)

#Add new row to the dataframe with loc

df.loc[len(df)] = [5,6]

#Drop a column/row  (when you do this it create a copy without removeing)
#If you want to effect the orginal one use inplace=True
dropped_value =  df.drop('B',axis=1)

dropped_value =  df.drop('B',axis=1,inplace=True)

print(df)
#Drop a row

print()

df.drop(0,axis=0,inplace=True)
print(df)
