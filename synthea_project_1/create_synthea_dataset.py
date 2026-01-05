import pandas as pd

df1 = pd.read_csv("allergies.csv")
df2 = pd.read_csv("careplans.csv")
print(df1.head())
print(df2.head())