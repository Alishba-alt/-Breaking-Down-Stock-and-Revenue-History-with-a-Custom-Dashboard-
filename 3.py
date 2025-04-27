import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2018, 2019, 2020, 2021, 2022],
    'Vehicle_Type': ['Sedan', 'Sedan', 'Sedan', 'Sedan', 'Sedan',
                     'SUV', 'SUV', 'SUV', 'SUV', 'SUV'],
    'Sales': [8000, 8500, 7800, 8200, 8000, 7000, 7300, 7100, 7500, 7400],
    'Period': ['Non-Recession', 'Non-Recession', 'Recession', 'Recession', 'Non-Recession',
               'Non-Recession', 'Non-Recession', 'Recession', 'Recession', 'Non-Recession']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the Seaborn style
sns.set(style='whitegrid')

# Create the line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Sales', hue='Vehicle_Type', style='Period', markers=True)

# Customize the plot
plt.title('Sales Trends by Vehicle Type: Recession vs Non-Recession', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales (in units)', fontsize=12)
plt.legend(title='Vehicle Type and Period')
plt.grid(True)
plt.show()