import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

shootings = pd.read_csv('shootings.csv')

shootings['date'] = pd.to_datetime(shootings['date'])
shootings['year'] = shootings['date'].apply(lambda x: x.year)

sns.jointplot(data=shootings, x='year', y='age', kind='hex', color='black')
plt.show()
