import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf

yf.pdr_override()

assets = ['TSLA', 'AAPL', 'MSFT', "IBM"]
startdate = '2019-01-01'
enddate = '2023-01-29'
data = pd.DataFrame()

for t in assets:
    data[t] = pdr.get_data_yahoo(t, start=startdate, end=enddate)['Adj Close']

#Charts

#Relative scale and base=100. (So every stock start from the same place in the chart)

(data / data.iloc[0]*100).plot(figsize=(12, 6)) #iloc[0] allow us to fix the denominator. #figsize allow us to represent in a specific size the chart
plt.show()