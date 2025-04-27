import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Waterfront': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No'],
        'Price': [500000, 300000, 320000, 800000, 310000, 900000, 290000, 750000, 330000, 280000]}
df = pd.DataFrame(data)

# Create boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Waterfront'], y=df['Price'])
plt.title('House Prices by Waterfront View')
plt.xlabel('Waterfront View')
plt.ylabel('Price')
plt.show()