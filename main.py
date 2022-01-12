# Load the Pandas libraries with alias 'pd'
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Accommodation.csv")

print(data.head())
print(data.columns)


sns.countplot(y='AddressRegion',hue='AddressCountry',data=data)
plt.show()
