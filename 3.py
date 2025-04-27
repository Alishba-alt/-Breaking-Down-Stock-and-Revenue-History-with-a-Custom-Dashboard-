import pandas as pd

# Sample DataFrame
data = {'Floor': [1, 2, 1, 3, 2, 3, 1, 2, 3, 1]}
df = pd.DataFrame(data)

# Count unique floor values and convert to DataFrame
floor_counts = df['Floor'].value_counts().to_frame()

# Display the result
print(floor_counts)