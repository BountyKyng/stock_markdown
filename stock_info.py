#Stock info reader
#Load required packages
import csv
import yfinance as yf
import pandas as pd
import numpy as np

#Set security
security = yf.Ticker("INTC")

#Stock price history
stock_history = security.history(period = "1y", interval = "1d")
stock_history.to_csv("data/stock_history.csv", sep = ",")

#Cashflow
cashflow = security.cashflow
cashflow.to_csv("data/cashflow.csv", sep = ",")

#Quarterly Balance Sheet
balance = security.quarterly_balance_sheet
balance.to_csv("data/balance.csv", sep = ",")

#Stock info
info = security.info

#company activitaties summary
summary = info['longBusinessSummary']
