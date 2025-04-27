import pandas as pd
import matplotlib.pyplot as plt

# Sample data for automobile sales
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Automobile_Sales': [15000, 17000, 16000, 18000, 17500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot a line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Automobile_Sales'], marker='o', linestyle='-', color='b')
plt.title('Yearly Automobile Sales', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales (in units)', fontsize=12)
plt.grid(True)
plt.show()