import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfboston = pd.read_csv('boston_weather.csv')
dfglobal = pd.read_csv('global_weather.csv')



boston_filled = dfboston.fillna(dfboston.mean())

boston_filled['moving_average'] = boston_filled.iloc[:,1].ewm(span=7,adjust=False).mean()

print(boston_filled.head(10))

