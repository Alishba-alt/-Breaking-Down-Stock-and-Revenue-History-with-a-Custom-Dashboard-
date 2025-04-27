import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [5000, 4800, 5200, 6000, 7000, 7200, 6800, 6900, 6100, 6500, 6300, 5500],
    'Seasonality': ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Fall', 'Fall', 'Fall', 'Winter']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Bubble sizes
bubble_sizes = [sales / 10 for sales in df['Sales']]

# Create a bubble plot
plt.figure(figsize=(12, 8))
plt.scatter(df['Month'], df['Sales'], s=bubble_sizes, alpha=0.6, c='blue', edgecolors='black')
plt.title('Impact of Seasonality on Automobile Sales', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (in units)', fontsize=12)
plt.grid(True)

# Annotate the plot with seasonality labels
for i in range(len(df)):
    plt.text(df['Month'][i], df['Sales'][i] + 200, df['Seasonality'][i], 
             fontsize=10, ha='center', color='darkred')

plt.show()