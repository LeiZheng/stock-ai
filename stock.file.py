import argparse
import os
import pathlib

import pandas as pd
# fix issue -- ImportError: cannot import name 'is_list_like'
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import pylab

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--stock", type=str, help="path to input video file", required=True)
ap.add_argument("-o", "--output", type=str, default="kcf", help="path to output video frames", required=True)
ap.add_argument("-sd", "--start_date", type=str, default="kcf", help="start time", required=True)
ap.add_argument("-ed", "--end_date", type=str, default="kcf", help="end", required=True)
args = vars(ap.parse_args())

tickName = args["stock"]
start_date = args["start_date"]
end_date = args["end_date"]
outputDir = args['output']

tickData = web.DataReader(name=tickName, data_source='tiingo', start=start_date, end=end_date,
               retry_count=3, pause=0.001, session=None, access_key='ebac00242c4f772b2497ae4a2b7a5d3952043b7a')

pathlib.Path(outputDir).mkdir(parents=True, exist_ok=True)

tickData.to_csv(os.path.join(outputDir, tickName + '.csv'))
