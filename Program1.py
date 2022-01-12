import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("netflix_titles_nov_2019.csv")

print(data.head())
print(data.columns)

sns.countplot(y='type',data=data)
plt.show()
