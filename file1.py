import seaborn as sns
import pandas as pd

# Load the dataset
df = sns.load_dataset("penguins")

# Preview
print(df.head())

df.iloc[:4, 1]

df.drop_duplicates()

new_column = {
"Adelie": "adel",
"Gentoo": "gent"

}

df["species_2"] = df["species"].map(new_column)

print(df)