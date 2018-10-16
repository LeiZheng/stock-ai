import argparse
import os
import pandas as pd
# fix issue -- ImportError: cannot import name 'is_list_like'
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import pylab

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", type=str, default="kcf", help="dir to load stock", required=True)
ap.add_argument("-s", "--stock", type=str, help="dir to load stock", required=True)
args = vars(ap.parse_args())

inputDir = args["input_dir"]
stock = args["stock"]

stockData = pd.read_csv(os.path.join(inputDir, stock + '.csv'))
print(stockData.head())
plt.figure(figsize = (18,9))
plt.plot(range(stockData.shape[0]),(stockData['adjLow']+stockData['adjHigh'])/2.0)
plt.xticks(range(0,stockData.shape[0],500),stockData['date'].loc[::500],rotation=45)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)
plt.show()

# First calculate the mid prices from the highest and lowest
high_prices = stockData.loc[:,'adjHigh'].as_matrix()
low_prices = stockData.loc[:,'adjLow'].as_matrix()
mid_prices = (high_prices+low_prices)/2.0

