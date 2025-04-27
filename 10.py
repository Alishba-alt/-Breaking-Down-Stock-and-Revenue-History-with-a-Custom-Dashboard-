from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np

# Example feature data (replace this with your actual data)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([1.1, 2.3, 3.0, 3.8, 5.1, 6.2, 7.4, 8.1, 9.5, 10.8])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform a second-order polynomial transformation
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Create and fit the Ridge regression model
ridge = Ridge(alpha=0.1)
ridge.fit(X_train_poly, y_train)

# Predict using test data
y_pred = ridge.predict(X_test_poly)

# Calculate R²
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')