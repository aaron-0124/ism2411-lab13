# Self-Assessment
# 1) A boolean filter selects rows that meet a certain condition.
# For example, it can show only sales from the South region.

# 2) df["revenue"] gives a Series, while df[["revenue"]]
# gives a DataFrame. This matters when working with
# multiple columns or functions that need a DataFrame.

# 3) I would choose pandas because it makes working with
# large amounts of data faster and easier than Excel.

import pandas as pd


# Exercise 1:
df = pd.read_csv("data/retail_sales.csv")

print("Exercise 1:")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# Exercise 2:
south = df[df["region"] == "South"]

print("\nExercise 2:")
print(len(south))
print(south.head())

# Exercise 3:
top_five = df.sort_values("revenue", ascending=False).head(5)

print("\nExercise 3:")
print(top_five)


# Exercise 4: 
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print("\nExercise 4:")
print(len(big_south))
print(big_south.head())


# Exercise 5: 
df["per_unit"] = df["revenue"] / df["quantity"]

print("\nExercise 5:")
print(df.head())
print(df["per_unit"].mean())


# Exercise 6:
print("\nExercise 6:")
print(df["region"].unique())
print(df["region"].value_counts())

# Exercise 7:
selected = df[["region", "product", "revenue"]]

print("\nExercise 7:")
print(selected.shape)


# Exercise 8: 
df.to_csv("data/explored.csv", index=False)

print("\nExercise 8:")
print("File saved successfully.")
