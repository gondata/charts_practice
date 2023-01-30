import pandas as pd
import plotly.graph_objects as go

def create_charts(df):
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'])])
    fig.show()
create_charts(pd.read_csv('NIO.csv'))