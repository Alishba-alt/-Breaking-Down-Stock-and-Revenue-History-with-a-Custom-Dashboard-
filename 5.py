import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'sqft_above': [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
        'price': [300000, 350000, 400000, 450000, 500000, 600000, 700000, 750000]}
df = pd.DataFrame(data)

# Create regression plot
plt.figure(figsize=(8, 6))
sns.regplot(x=df['sqft_above'], y=df['price'])
plt.title('Correlation Between Sqft Above and Price')
plt.xlabel('Sqft Above')
plt.ylabel('Price')
plt.show()