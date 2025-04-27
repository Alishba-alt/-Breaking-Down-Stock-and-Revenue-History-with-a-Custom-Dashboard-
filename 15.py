import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame for Yearly Report Statistics
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Total_Sales': [80000, 85000, 78000, 82000, 80000],
    'Total_Revenue': [500000, 520000, 480000, 510000, 500000],
    'Total_Profit': [100000, 120000, 90000, 110000, 100000]
}
df = pd.DataFrame(data)

# Matplotlib: Line Plot for Sales, Revenue, and Profit
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Total_Sales'], marker='o', label='Total Sales', color='blue')
plt.plot(df['Year'], df['Total_Revenue'], marker='o', label='Total Revenue', color='green')
plt.plot(df['Year'], df['Total_Profit'], marker='o', label='Total Profit', color='orange')
plt.title('Yearly Trends: Sales, Revenue, and Profit', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Amount (in USD)', fontsize=12)
plt.legend(title="Metrics")
plt.grid(True)
plt.show()

# Seaborn: Bar Chart for Total Sales by Year
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Total_Sales', data=df, palette='Blues_d')
plt.title('Total Sales by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales (in USD)', fontsize=12)
plt.show()

# Matplotlib: Pie Chart for Revenue Contribution
plt.figure(figsize=(8, 8))
plt.pie(
    df['Total_Revenue'],
    labels=df['Year'],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette('pastel'),
    explode=(0, 0, 0.1, 0, 0),  # Highlighting the year 2020
    shadow=True
)
plt.title('Revenue Contribution by Year', fontsize=16)
plt.show()