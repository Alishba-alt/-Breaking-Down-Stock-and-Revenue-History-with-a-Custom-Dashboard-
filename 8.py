from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Example feature data (replace this with your actual data)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2.1, 2.9, 3.7, 4.1, 5.2])

# Create the pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Scale the data
    ('poly', PolynomialFeatures(degree=2)),  # Polynomial transformation
    ('linear', LinearRegression())  # Linear regression model
])

# Fit the model
pipeline.fit(X, y)

# Predict
y_pred = pipeline.predict(X)

# Calculate R²
r2 = r2_score(y, y_pred)
print(f'R² Score: {r2}')