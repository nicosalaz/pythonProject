import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality.head())

#air_quality.plot()
#plt.show()

air_quality["station_antwerp"][0] = np.mean(air_quality["station_antwerp"])
print(air_quality["station_antwerp"][0])