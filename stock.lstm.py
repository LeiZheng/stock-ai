import argparse
import os
import pandas as pd

# fix issue -- ImportError: cannot import name 'is_list_like'
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import pylab

from sklearn.preprocessing import MinMaxScaler

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", type=str, default="kcf", help="dir to load stock", required=True)
ap.add_argument("-s", "--stock", type=str, help="dir to load stock", required=True)
args = vars(ap.parse_args())

inputDir = args["input_dir"]
stock = args["stock"]

stockData = pd.read_csv(os.path.join(inputDir, stock + '.csv'), delimiter=',',
                        usecols=['date', 'adjOpen', 'adjHigh', 'adjLow', 'adjClose'])
print(stockData.head())
plt.figure(figsize=(18, 9))
plt.plot(range(stockData.shape[0]), (stockData['adjLow'] + stockData['adjHigh']) / 2.0)
plt.xticks(range(0, stockData.shape[0], 500), stockData['date'].loc[::500], rotation=45)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Mid Price', fontsize=18)
# plt.show()
# First calculate the mid prices from the highest and lowest
high_prices = stockData.loc[:, 'adjHigh'].as_matrix()
low_prices = stockData.loc[:, 'adjLow'].as_matrix()
mid_prices = (high_prices + low_prices) / 2.0
print(stockData.shape)
print(mid_prices.shape)

# seperate the data to train and test data.
count = int(mid_prices.shape[0] / 10 * 9)
train_data = mid_prices[:count]
test_data = mid_prices[count:]

# Scale the data to be between 0 and 1
# When scaling remember! You normalize both test and train data with respect to training data
# Because you are not supposed to have access to test data
scaler = MinMaxScaler()
print(train_data)
train_data = train_data.reshape(-1,1)
test_data = test_data.reshape(-1,1)
print(train_data)
smoothing_window_size =  int(count / 3)
for di in range(0,count,smoothing_window_size):
    scaler.fit(train_data[di:di+smoothing_window_size,:])
    train_data[di:di+smoothing_window_size,:] = scaler.transform(train_data[di:di+smoothing_window_size,:])


