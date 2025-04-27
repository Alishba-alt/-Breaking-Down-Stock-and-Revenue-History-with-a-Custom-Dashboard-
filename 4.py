import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'GDP_Recession': [2.5, 1.8, -1.5, 0.5, 1.0],
    'GDP_NonRecession': [3.0, 2.8, 3.2, 3.1, 3.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Plot GDP during recession
ax[0].plot(df['Year'], df['GDP_Recession'], marker='o', color='r')
ax[0].set_title('GDP During Recession Period', fontsize=14)
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('GDP Growth (%)', fontsize=12)
ax[0].grid(True)

# Plot GDP during non-recession
ax[1].plot(df['Year'], df['GDP_NonRecession'], marker='o', color='g')
ax[1].set_title('GDP During Non-Recession Period', fontsize=14)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()