# *Assignment (24/02/2026)*

# *Assignment Name* : Dataset Detective
# *Description* : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.

import pandas as pd

df = pd.read_csv("data.csv")

print("Top 5 Rows:")
print(df.head())

print("\nHighest Value in Each Column:")
print(df.max(numeric_only=True))

print("\nMissing Values Count:")
print(df.isnull().sum())

