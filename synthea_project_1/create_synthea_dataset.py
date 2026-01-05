import pandas as pd
import duckdb
import numpy as np

# Set pandas display options to show all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df1 = pd.read_csv("allergies.csv")
df2 = pd.read_csv("careplans.csv")
print(df1.head())
print(df2.head())

con = duckdb.connect()

query = """
SELECT
    COUNT(ENCOUNTER) AS total_encounters
FROM read_csv_auto('allergies.csv')
"""

df1 = con.execute(query).fetchdf()
print("Column names:", list(df1.columns))
print(df1)

# Test numpy
print("NumPy version:", np.__version__)
print("NumPy array test:", np.array([1, 2, 3]))