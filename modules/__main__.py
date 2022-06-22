# This script is used to automate the download of ticker information

# Import required packages
import os
import yfinance as yf
import pandas as pd
import numpy as np

# Import custom modules
import COMPANIES
import STOCK_HISTORY

# Toggles for table parts
vLoad_Companies = False
vLoad_Stocks = True

# Set path
path = "C:/Users/ceyla/Downloads/"

# Set tickers to download and collect data from
Tickers = ['INTC', 'AMD']
start_date = "2021-01-01"
end_date = "2021-12-31"

# Statement for vLoad_Companies
if vLoad_Companies:
    COMPANIES.companies(Tickers)

# Statement for vLoad_Stocks
if vLoad_Stocks:
    STOCK_HISTORY.stock_history(Tickers, start_date, end_date)