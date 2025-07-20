import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# READING A DATA SET
df = pd.read_csv("C:\\Users\\DELL\Desktop\\food_delivery_data.csv")

# Print first 5 rows
print(df)
print(df.head())              # First few rows
print(df.shape)               # Rows and columns
print(df.info())              # Data types
print(df.describe())          # Numerical summary
print(df.columns)
