import matplotlib.pyplot as plt

# Sample data for advertisement expenditure during recession
data = {
    'Vehicle_Type': ['Sedan', 'SUV', 'Truck', 'Hatchback'],
    'Advertisement_Expenditure': [15000, 20000, 12000, 8000]  # Replace with actual values
}

# Pie chart labels and sizes
labels = data['Vehicle_Type']
sizes = data['Advertisement_Expenditure']
colors = ['gold', 'lightblue', 'lightgreen', 'orange']  # Custom colors for vehicle types
explode = [0.1 if x == 'SUV' else 0 for x in labels]  # Highlighting SUV

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title('Advertisement Expenditure by Vehicle Type During Recession Period', fontsize=16)
plt.show()