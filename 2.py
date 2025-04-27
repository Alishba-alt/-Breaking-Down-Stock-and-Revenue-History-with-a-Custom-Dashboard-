import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sedan': [8000, 8500, 7800, 8200, 8000],
    'SUV': [7000, 7300, 7100, 7500, 7400],
    'Truck': [5000, 5200, 4800, 5100, 5050]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot line chart for vehicle types
plt.figure(figsize=(10, 6))
for category in df.columns[1:]:
    plt.plot(df['Year'], df[category], marker='o', label=category)

plt.title('Sales Trends by Vehicle Type', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales (in units)', fontsize=12)
plt.legend(title='Vehicle Type')
plt.grid(True)
plt.show()