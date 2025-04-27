import pandas as pd

# Sample DataFrame
data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C'], 'Column3': [1.1, 2.2, 3.3]}
df = pd.DataFrame(data)

# Display data types
print(df.dtypes)