import pandas as pd

# Read the raw data
df = pd.read_csv("data/sample_data.csv")

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Select numeric columns
numeric_columns = df.select_dtypes(include="number").columns

# Fill missing numeric values with column mean
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaned data saved to data/cleaned_data.csv")
print("Missing values after cleaning:")
print(df.isnull().sum())