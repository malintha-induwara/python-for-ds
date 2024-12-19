#You are a data analyst for a retail company , the company has provided you with the following table containing sales data
# 1. Use Pandas to load the table into a DataFrame
# 2. Add a new column total revenue that caluclates the total revenue for each order
# 3. Idenitfy the best selling product(s)

# Order ID Product Category Quantity  Price
# 101   Laptop  Electronics  2  1000
# 102   SmartPhone  Electronics  5  200
# 103   DeskChair Furniture  10  150
# 104   Monitor Electronics  4  200
# 105   Bookshelf Furniture  2  300

import pandas as pd

data = {'Order ID':[101,102,103,104,105],
        'Product':['Laptop','SmartPhone','DeskChair','Monitor','Bookshelf'],
        'Category':['Electronics','Electronics','Furniture','Electronics','Furniture'],
        'Quantity':[2,5,10,4,2],
        'Price':[1000,200,150,200,300]}

df = pd.DataFrame(data)

df['Total Revenue'] = df['Quantity'] * df['Price']

#print(df)   

best_selling_product = df[df['Quantity'] == df['Quantity'].max()]

print(best_selling_product)

sorted_df = df.sort_values(by='Quantity')

print(sorted_df)


