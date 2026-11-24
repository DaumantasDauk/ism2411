#self assesment:
#1. Flagging seems most tricky for me, since it involves recognising unique values using code
# I would hope to learn more about how python can filter unique values (F.E. regex)
#2. The comments are short by design and in my opinion, readable, but some could argue - too short. 
#3. After running describe, I noticed clear indocators of outliers  
import pandas as pd

#----ex1---
df = pd.read_csv('data/messy_sales.csv')
df.info()
print(df.isnull().sum())

#issues:
#1. product category cant return a number
#2. Unit price return 0
#3. quantity sold is float64 Dtype

#----ex2---
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns.tolist())

#---ex3---

print("Shape before changes:", df.shape)
# fill in the missing values in the "quantity_sold" column with the mean of the column
df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())
#withou order id or date, information is not useful 
df = df.dropna(subset=["order_id", "order_date"])
print("Shape after changes:", df.shape)
print(df.isnull().sum())

#---ex4---
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print(" NaT:", df["order_date"].isna().sum())
df["unit_price"] = (
    df["unit_price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
df["quantity_sold"] = df["quantity_sold"].astype(int)
df["revenue"] = (df["unit_price"] * df["quantity_sold"])
print(df.dtypes)

#---ex5---
print("identicalrows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after dropping:", df.shape)

#---ex6---
print(df.describe())
#negative values observed in min
#-could potentially be a return or an error  
#mean is above 75percentile 
#-one placeholder value is impacting the data 
#mean is way higher than the median
#-might mean large outliers are present

df = df[df["quantity_sold"] != 9999]
print("Shape after removing 9,999 placeholder rows:", df.shape)
print(df.describe())

#---ex7---

df.to_csv("data/clean_sales.csv", index=False)
df_reloaded = pd.read_csv("data/clean_sales.csv")
print(" Reloaded w/o parse_dates ")
df_reloaded.info()

df_clean = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])
print("\n Reloaded with parse_dates ")
df_clean.info()