import pandas as pd
import matplotlib.pyplot as plt

# Sample data for average vehicle price and sales volume during a recession
data = {
    'Average_Price': [20000, 25000, 22000, 27000, 23000],
    'Sales_Volume': [8000, 7000, 8500, 6000, 7800],
    'Year': [2018, 2019, 2020, 2021, 2022]  # Optional for annotation
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Average_Price'], df['Sales_Volume'], c='blue', edgecolors='black', alpha=0.6)
plt.title('Correlation Between Average Vehicle Price and Sales Volume During Recession', fontsize=16)
plt.xlabel('Average Vehicle Price (USD)', fontsize=12)
plt.ylabel('Sales Volume (Units)', fontsize=12)
plt.grid(True)

# Optional: Annotate points with years for better clarity
for i in range(len(df)):
    plt.text(df['Average_Price'][i] + 200, df['Sales_Volume'][i], str(df['Year'][i]), 
             fontsize=10, color='darkred')

plt.show()