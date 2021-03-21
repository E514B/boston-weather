import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfboston = pd.read_csv('boston_weather.csv')
dfglobal = pd.read_csv('global_weather.csv')

boston_filled = dfboston.fillna(dfboston.mean())

boston_filled['MA_7(omit 6)'] = boston_filled.avg_temp.rolling(7).mean()

dfglobal['MA_7(omit 6)'] = dfglobal.avg_temp.rolling(7).mean()

print(boston_filled)
print(dfglobal)

plt.plot(boston_filled.year, boston_filled['MA_7(omit 6)'], label='Boston temp')
plt.plot(dfglobal.year, dfglobal['MA_7(omit 6)'], label='Global temp')

plt.xlabel("Year")
plt.ylabel("7 year temperature average")
plt.title("Boston vs. Global Temperature Comparison")
plt.legend()
plt.show()