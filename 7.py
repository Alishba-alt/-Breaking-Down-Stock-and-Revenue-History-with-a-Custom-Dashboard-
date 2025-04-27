import matplotlib.pyplot as plt

# Sample data
data = {
    'Period': ['Recession', 'Non-Recession'],
    'Advertising_Expenditure': [40000, 60000]  # Replace with actual expenditure values
}

# Pie chart labels and sizes
labels = data['Period']
sizes = data['Advertising_Expenditure']
colors = ['lightcoral', 'skyblue']  # Custom colors for the periods
explode = (0.1, 0)  # Explode the slice for Recession

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title('Advertising Expenditure During Recession and Non-Recession Periods', fontsize=16)
plt.show()