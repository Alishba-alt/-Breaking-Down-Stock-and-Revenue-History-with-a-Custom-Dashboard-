import pandas as pd

# Sample DataFrame
data = {'id': [101, 102, 103], 'Unnamed: 0': [0, 1, 2], 'Column1': [10, 20, 30], 'Column2': [1.5, 2.5, 3.5]}
df = pd.DataFrame(data)

# Drop columns and modify DataFrame in place
df.drop(['id', 'Unnamed: 0'], axis=1, inplace=True)

# Get statistical summary
print(df.describe())