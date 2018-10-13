import argparse
import datetime as dt
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import pylab

# fix issue -- ImportError: cannot import name 'is_list_like'
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str,
	help="path to save stock data")
ap.add_argument("-s", "--stock", type=str,
	help="stock name to pick")
ap.add_argument("-s", "--startdate", type=datetime, default=0.5,
	help="include the start time")
ap.add_argument("-e", "--enddate", type=datetime, default=320,
	help="the end of date.")

ap.add_argument("-e", "--height", type=int, default=320,
	help="nearest multiple of 32 for resized height")
ap.add_argument("-p", "--padding", type=float, default=0.0,
	help="amount of padding to add to each border of ROI")
args = vars(ap.parse_args())

