import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfboston = pd.read_csv('boston_weather.csv')
dfglobal = pd.read_csv('global_weather.csv')

print('The average temperature for Boston across the data set is', dfboston.avg_temp.mean())
print('The average temperature for the globe across the data set is', dfglobal.avg_temp.mean())


boston_filled = dfboston.fillna(dfboston.mean())

boston_filled['MA_20'] = boston_filled.avg_temp.rolling(20).mean()

dfglobal['MA_20'] = dfglobal.avg_temp.rolling(20).mean()

print(boston_filled)
print(dfglobal)

plt.plot(dfglobal.year, dfglobal['MA_20'], label='Global')
plt.plot(boston_filled.year, boston_filled['MA_20'], label='Boston')


plt.xlabel("Year")
plt.ylabel("Temperature °C")
plt.title("Line Chart of Global vs. Boston Temperature \n (20 Year Moving Average)")
plt.legend()
plt.show()