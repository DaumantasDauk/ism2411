#boolean filter simply selects rows that meets the requirements you specified in the code
#[] only captures a single dimension of data, while [[]] captires 2 dimensions (a table)
# the reason we use pandas is speed - it is way faster than excel, it is also cheaper than using AI models (and faster)

#---ex1---
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

#---ex2---
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

#---ex3---
top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

#---ex4---
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

#---ex5---
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

#---ex6---
#method1
print(df['region'].unique())

#method2
print(df['region'].value_counts())

#---ex7---
new_DataFrame = df[['region', 'product', 'revenue']]
print(new_DataFrame.shape)

#----ex8---
df.to_csv('data/retail_sales_copy.csv', index=False)