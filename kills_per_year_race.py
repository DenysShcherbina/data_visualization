import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

shootings = pd.read_csv('shootings.csv')

shootings['date'] = pd.to_datetime(shootings['date'])
shootings['year'] = shootings['date'].apply(lambda x: x.year)

sns.countplot(data=shootings, x='year', hue='race', palette='coolwarm')
plt.title('Kills per year divided by race')
plt.show()
