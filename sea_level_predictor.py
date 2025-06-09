import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

df = pd.read_csv('epa-sea-level.csv')

plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

df_cleaned = df.dropna(subset=['CSIRO Adjusted Sea Level'])
res = linregress(df_cleaned['Year'], df_cleaned['CSIRO Adjusted Sea Level'])
print(res)
x_1 = pd.Series([i for i in range(1880, 2051)])
y_1 = res.slope*x_1 + res.intercept
plt.plot(x_1, y_1, 'r')

new_df = df[df['Year'] >= 2000].dropna(subset=['CSIRO Adjusted Sea Level'])
x_new = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
x_pred = pd.Series(i for i in range(2000, 2051))
y_pred = x_new.slope*x_pred + x_new.intercept
plt.plot(x_pred, y_pred, "green")

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

plt.savefig('sea_level_plot.png')