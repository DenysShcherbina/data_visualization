import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create DataFrame from CSV
shootings = pd.read_csv('shootings.csv')

# Convert type of data in column
shootings['date'] = pd.to_datetime(shootings['date'])

# Create new columns
shootings['month'] = shootings['date'].apply(lambda x: x.month)
shootings['day'] = shootings['date'].apply(lambda x: x.day)

# Create pivot table for heatmap
month_day = shootings.pivot_table(values=shootings, index='day', columns='month', aggfunc='count')['age']

plt.figure(figsize=(10, 6))
sns.heatmap(data=month_day, cmap='plasma', annot=True, linewidths=0.5)
plt.title('Month_day')
plt.show()
