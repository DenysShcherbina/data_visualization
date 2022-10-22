import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def category_age(age):
    if age <= 10:
        return '0-10'
    elif 10 < age <= 20:
        return '11-20'
    elif 20 < age <= 25:
        return '21-25'
    elif 25 < age <= 30:
        return '26-30'
    elif 30 < age <= 35:
        return '31-35'
    elif 35 < age <= 40:
        return '36-40'
    elif 40 < age <= 45:
        return '41-45'
    elif 45 < age <= 50:
        return '46-50'
    elif 50 < age <= 55:
        return '51-55'
    elif 55 < age <= 60:
        return '56-60'
    elif 60 < age <= 70:
        return '61-70'
    elif 70 < age <= 80:
        return '71-80'
    else:
        return '81-100'


shootings = pd.read_csv('shootings.csv')

shootings['date'] = pd.to_datetime(shootings['date'])
shootings['year'] = shootings['date'].apply(lambda x: x.year)

shootings['category_age'] = shootings['age'].apply(category_age)
sns.countplot(data=shootings.sort_values(by='category_age'), x='category_age', hue='race')
plt.title('By age category')
plt.tight_layout()
plt.show()
