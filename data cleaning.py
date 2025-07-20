import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\food_delivery_data.csv")

# 2. Clean column names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

# 3. Basic info
print("Initial Overview:")
print(df.head())
print("\nShape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
df.columns = df.columns.str.strip()
print(df.columns)

# 4. Convert categorical columns
df['Traffic_conditions'] = df['Traffic_conditions'].astype('category')
df['Weather_conditions'] = df['Weather_conditions'].astype('category')

# 5. Handle missing values (if any)

## checking for duplicates again
print("Duplicates:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
## standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns)
## CHECK FOR ZERO OR NULL VALUES
print((df['distance'] <= 0).sum())

##  CLEANED NAME OF COLUMNS
print(df.columns.tolist())

import pandas as pd

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['time_taken_(min)'].quantile(0.25)
Q3 = df['time_taken_(min)'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the DataFrame to remove outliers
df_no_outliers = df[(df['time_taken_(min)'] >= lower_bound) & (df['time_taken_(min)'] <= upper_bound)]

# Print shape to compare
print("Original shape:", df.shape)
print("After removing outliers (IQR method):", df_no_outliers.shape)
## CLEANED DATA
df_no_outliers.to_csv("cleaned_data.csv", index=False)

