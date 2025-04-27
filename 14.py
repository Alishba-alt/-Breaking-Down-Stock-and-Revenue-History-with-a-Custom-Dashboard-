import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data for the recession report
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'GDP_Growth': [2.5, 2.0, -3.5, 1.5, 3.0],
    'Unemployment_Rate': [4.0, 3.8, 8.5, 6.0, 5.0],
    'Consumer_Spending': [30000, 32000, 25000, 28000, 31000],
    'Automobile_Sales': [15000, 17000, 16000, 18000, 17500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create and display GDP growth graph
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['GDP_Growth'], marker='o', linestyle='-', color='blue')
plt.title('GDP Growth During Recession Periods', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP Growth (%)', fontsize=12)
plt.grid(True)
plt.show()

# Create and display unemployment rate graph
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Unemployment_Rate'], marker='o', linestyle='-', color='red')
plt.title('Unemployment Rate During Recession Periods', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.grid(True)
plt.show()

# Create and display consumer spending graph
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Consumer_Spending'], marker='o', linestyle='-', color='green')
plt.title('Consumer Spending Trends During Recession Periods', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Consumer Spending (in USD)', fontsize=12)
plt.grid(True)
plt.show()

# Create an interactive graph for automobile sales using Plotly
fig = px.line(df, x='Year', y='Automobile_Sales', title='Automobile Sales Trends During Recession Periods',
              labels={'Year': 'Year', 'Automobile_Sales': 'Automobile Sales (Units)'})
fig.show()