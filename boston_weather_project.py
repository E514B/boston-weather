import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfboston = pd.read_csv('boston_weather.csv')
dfglobal = pd.read_csv('global_weather.csv')



boston_filled = dfboston.fillna(dfboston.mean())

boston_filled['MA_7'] = boston_filled.avg_temp.rolling(7).mean().shift(-6)

print(boston_filled.tail(20))



