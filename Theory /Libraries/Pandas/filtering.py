import pandas as pd

data = {'Name':['Alice','Bob','Charile','David'],
        'Age':[24,27,22,32],
        'Score':[85,70,90,98]}

df = pd.DataFrame(data)
print(df)


filterd_data = df[df['Age'] > 25]

print(filterd_data)
print(type(filterd_data))
