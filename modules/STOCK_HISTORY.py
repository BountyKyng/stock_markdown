# This function creates the STOCK_HISTORY table from the data model. 

# Import required packages
import os
import yfinance as yf
import pandas as pd
import numpy as np

# Create function to download stock data
def stock_history(x, y, z):

    # Create the companies dataframe
    STOCK_HISTORY = pd.DataFrame(columns=['COMPANY',
                                     'Stock Date',
                                     'Stock Open',
                                     'Stock High',
                                     'Stock Low',
                                     'Stock Close',
                                     'Stock Adj Close',
                                     'Stock Volume'])

    # Loop through Tickers list to download data
    for i in x:
        
        # Download stock data with given time frame
        data = yf.download(i, start = y, end = z)

        # Reset the index
        data.reset_index(inplace = True)

        # Add ticker value to the stock history table
        data['COMPANY'] = i

        # Rename columns to match data model
        data = data.rename(columns={'Date':'Stock Date',
                    'Open':'Stock Open',
                    'High':'Stock High',
                    'Low':'Stock Low',
                    'Close':'Stock Close',
                    'Adj Close':'Stock Adj Close',
                    'Volume':'Stock Volume'})

        # Concat STOCK_HISTORY table with data for each ticker
        STOCK_HISTORY = pd.concat(objs=[STOCK_HISTORY, data])

    # Write STOCK_HISTORY table to data folder
    # Seperated by '|'
    # mode 'w'
    STOCK_HISTORY.to_csv('data/STOCK_HISTORY.txt', index=None, sep='|', mode='w')
