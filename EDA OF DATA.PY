import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# GIVEN A PATH FOR MY FILE
df = pd.read_csv("C:\\Users\\DELL\Desktop\\food_delivery_data.csv")

# Print first 5 rows
print(df)
print(df.head())              # First few rows
print(df.shape)               # Rows and columns
print(df.info())              # Data types
print(df.describe())          # Numerical summary
print(df.columns)


## EDA PROCESS OF MY DATA
import seaborn as sns
import matplotlib.pyplot as plt

# Plot
sns.countplot(x='Traffic_conditions', data=df)
plt.title('Traffic Conditions Distribution')

# Save before showing
plt.savefig("traffic_conditions_plot.png", dpi=300, bbox_inches='tight')  # or .jpg/.pdf

# Show the plot
plt.show()



# Delivery time vs Traffic
import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot: Delivery time vs Traffic conditions
sns.boxplot(x='Traffic_conditions', y='Time_taken (min)', data=df)
plt.title('Delivery Time vs Traffic Conditions')
plt.xlabel('Traffic Conditions')
plt.ylabel('Time Taken (min)')

# Save the plot
plt.savefig("delivery_time_vs_traffic_conditions.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

# Pair plot (only on numerical columns)
sns.pairplot(df)
plt.savefig('pairplot.png')  # Save pairplot
plt.show()

# Correlation heatmap
import numpy as np
import pandas as pd

# Compute correlation only on numeric columns
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig('correlation_heatmap.png')  # Save heatmap
plt.show()