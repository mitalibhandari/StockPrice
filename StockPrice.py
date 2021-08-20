import yfinance as yf
import streamlit as st
import pandas as pd


# Markdown language
# heading
st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

# Define the ticker Symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
# period is one day
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')
# Open High Low Close  Volume Dividents Stock splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
