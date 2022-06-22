# This function creates the COMPANIES table from the data model. 

# Import required packages
import os
import yfinance as yf
import pandas as pd
import numpy as np

# Create function 
def companies(x):

    # Create the companies dataframe
    COMPANIES = pd.DataFrame(columns=['COMPANY',
                                     'Company Name',
                                     'Company Ticker',
                                     'Company Sector',
                                     'Company Industry',
                                     'Company Country'])

    # Loop through list of tickers
    for i in x:
        
        # Get Ticker info and data
        ticker = yf.Ticker(i)
        info = ticker.info

        # Create correct dataframe from Ticker info
        info = pd.DataFrame.from_dict(info, orient='index')
        info = info.reset_index()
        info.columns = ['Class', 'Data']
        info = info.transpose()
        info.columns = info.iloc[0]
        info = info.drop(index='Class')
        info = info[['sector','symbol', 'industry', 'country', 'longName']]

        # Rename columns to match data model
        info = info.rename(columns={'symbol':'Company Ticker',
                            'industry':'Company Industry',
                            'country':'Company Country',
                            'longName':'Company Name',
                            'sector':'Company Sector'})

        # Add primary key to data
        info['COMPANY'] = info['Company Ticker']
        
        # Concat COMPANY table with data for each ticker
        COMPANIES = pd.concat(objs=[COMPANIES, info])
        
        # Write COMPANIES table to data folder
        # Seperated by '|'
        # mode 'w'
        COMPANIES.to_csv('data/COMPANIES.txt', index=None, sep='|', mode='w')




