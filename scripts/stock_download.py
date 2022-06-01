# This script is used to automate the download of ticker information

# Import required packages
import yfinance as yf
import pandas as pd
import numpy as np

# Toggles for table parts
vLoad_Stocks = True

# Set tickers to download and collect data from
Tickers = ['INTC', 'AMD']
start_date = "2021-01-01"
end_date = "2021-12-31"

# Create Company table
# The Company table is a permanent table in the data model



















# Code for vLoad_Stocks
if vLoad_Stocks:
    # Initialise Ticker dictionary to loop through.
    Ticker_df = {}

    # Download stock history based on tickers in the Tickers list
    for Ticker in Tickers:
        Ticker_df[Ticker] = yf.download(Ticker, start = start_date, end = end_date)

    for i in Ticker_df:    
        globals()[i]=Ticker_df[i]

    for i in Tickers:
        globals()[i]['Company'] = i

    for i in Tickers:
        globals()[i] = globals()[i].reset_index(level=0)

    #data = pd.concat([AMD, INTC], ignore_index = False)