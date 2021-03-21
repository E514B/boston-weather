import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfboston = pd.read_csv('boston_weather.csv')
dfglobal = pd.read_csv('global_weather.csv')



boston_filled = dfboston.fillna(dfboston.mean())

boston_filled['MA_7(omit 6)'] = boston_filled.avg_temp.rolling(7).mean()

boston_filled['MA_7'] = boston_filled.avg_temp.rolling(7, min_periods=1).mean()

dfglobal['MA_7(omit 6)'] = dfglobal.avg_temp.rolling(7).mean()

dfglobal['MA_7'] = dfglobal.avg_temp.rolling(7, min_periods=1).mean()

print(dfglobal.head(10))
print(boston_filled.head(10))
