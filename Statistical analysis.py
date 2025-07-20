import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make sure this path is correct and matches your file location
df = pd.read_csv("C:\\Users\\DELL\Desktop\\food_delivery_data.csv")

# Average delivery time per traffic condition
print(df.groupby('Traffic_conditions')['Time_taken (min)'].mean())

# Weather impact
print(df.groupby('Weather_conditions')['Time_taken (min)'].describe())
