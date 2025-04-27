import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample DataFrame
data = {'sqft_living': [1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],
        'price': [320000, 350000, 375000, 400000, 425000, 450000, 475000, 500000, 525000, 550000]}
df = pd.DataFrame(data)

# Reshape sqft_living for model
X = df[['sqft_living']]
y = df['price']

# Fit Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Predict prices
y_pred = model.predict(X)

# Calculate R² score
r2 = r2_score(y, y_pred)

# Print the R² score
print(f'R² Score: {r2}')

# Visualize regression line
plt.figure(figsize=(8, 6))
plt.scatter(df['sqft_living'], df['price'], label="Actual Data")
plt.plot(df['sqft_living'], y_pred, color='red', label="Regression Line")
plt.xlabel("Sqft Living")
plt.ylabel("Price")
plt.title("Linear Regression: Sqft Living vs. Price")
plt.legend()
plt.show()