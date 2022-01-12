import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv("netflix_titles_nov_2019.csv")

print(data.head())
print(data.columns)

plt.figure(figsize=(5,7))
sns.set(style="darkgrid")
ax = sns.countplot(x="rating", data=data, palette="Set2", order=data['rating'].value_counts().index[0:15])