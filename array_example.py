import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make sure this path is correct and matches your file location
df = pd.read_csv("C:\\Users\\DELL\Desktop\\food_delivery_data.csv")

# Print first 5 rows
print(df)
print(df.head())              # First few rows
print(df.shape)               # Rows and columns
print(df.info())              # Data types
print(df.describe())          # Numerical summary
print(df.columns)

## DATA CLEANING STEPS START HERE
## STEP TO CHECK THE MISSING VALUES IF ANY
print(df.isnull().sum())      # Missing values

## FIX INCONSISTENT CATEGORICAL ENTRIES
df['Traffic_conditions'] = df['Traffic_conditions'].str.strip().str.title()
df['Weather_conditions'] = df['Weather_conditions'].str.strip().str.title()

# Optional: Clean column names to avoid issues
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Now safely use cleaned column name
Q1 = df['Time_taken(min)'].quantile(0.25)
Q3 = df['Time_taken(min)'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_no_outliers = df[(df['Time_taken(min)'] >= lower_bound) & (df['Time_taken(min)'] <= upper_bound)]

# Optional: Print shape to compare
print("Original:", df.shape)
print("Without outliers:", df_no_outliers.shape)




## CONVERTING MYFOLLOWING COLUMN INTO CATEGORY WHICH CONSUMES LESS MEMORY
df['Traffic_conditions'] = df['Traffic_conditions'].astype('category')
df['Weather_conditions'] = df['Weather_conditions'].astype('category')


## EDA PROCESS STARTS HERE 

sns.countplot(x='Traffic_conditions', data=df)
## ABOVE METHOD HELPS TO TELL HOW MANY TIMES EACH CATEGORY APPEARED IN MY DATAFRAME.
plt.title('Traffic Conditions Distribution')
plt.show()

