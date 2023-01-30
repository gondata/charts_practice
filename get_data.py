from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

y_symbols = ['NIO']
startdate = '2020-01-01'
enddate = '2023-01-29'

for i in y_symbols:
    pdr.get_data_yahoo(i, start=startdate, end=enddate).to_csv(i+".csv")