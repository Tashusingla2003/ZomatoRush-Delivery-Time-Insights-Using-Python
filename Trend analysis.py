import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make sure this path is correct and matches your file location
df = pd.read_csv("C:\\Users\\DELL\Desktop\\food_delivery_data.csv")

# Mean delivery time by order hour
hourly = df.groupby('Order_Hour')['Time_taken (min)'].mean().reset_index()

# Line plot
plt.figure(figsize=(10,5))
plt.plot(hourly['Order_Hour'], hourly['Time_taken (min)'], marker='o')
plt.title("Average Delivery Time by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Time Taken (min)")
plt.grid(True)
plt.tight_layout()
plt.savefig("delivery_time_hourly_trend.png")
plt.show()
