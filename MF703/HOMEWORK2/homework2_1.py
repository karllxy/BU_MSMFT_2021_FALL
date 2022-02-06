# 
# homework2-1.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: 1.Historical Analysis of Sector ETFs
#              
# 

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pandas_datareader import data
from sklearn import linear_model
from sklearn.metrics import mean_squared_error as MSE
from statsmodels.tsa.ar_model import AR
import statsmodels.api as sm

#1. Historical Analysis of Sector ETFs:
    

#(a) Download and Clean/Check the data for splits and other anomalies

def collect_data(stocks, source, start_dates, end_dates):
    
    Data = data.DataReader(stocks, source, start_dates, end_dates)
    adj = Data['Adj Close']
    
    condition = adj.isnull().any()
    


    for i in range(len(adj.iloc[0,0:])): #  Use 'if' sentence to check whether each line lose data or not
        
        if condition[i] == True:
            adj.iloc[:,i] = adj.iloc[:,i].fillna( method='ffill') # Here I assume that there weren't be a large amount NAN data in these ETFs, so I use former data to fill NAN if possible.
    
    return adj


def returns(adj):     
    
    df = adj / adj.shift(1) - 1
    df = df.iloc[1:] # The first raw of df would be NAN since there's no more data to calculate its returns, so I just drop it.
    
    return df 


#(b) Calculate the annualized return and standard deviation of each ETF:

def compute_returns_vol(df):
    
    mean_return = df.mean()
    annual_return = mean_return * 252 # Using mean daily return for each ticker, Multiplying them  by 252 to annualize the returns.
    
    annual_std = df.std() * (252 ** 0.5)
    
    index = annual_return.index
    table = pd.DataFrame(index = index, columns = ['Annualized Returns','Annualized Standard Deviation'])
    table['Annualized Returns'] = annual_return
    table['Annualized Standard Deviation'] = annual_std
    
    return table


#(c). Compute a covariance matrix of daily and monthly  returns for the set of ETFs

def compute_corre_mat(df):
    
    day_corre_mat = df.cov()
    
    month_corre_mat = df.resample('M').sum().cov()
    
    print('Covariance Matrix of Daily Returns: ')
    print(day_corre_mat)
    print()
    print('Covariance Matrix of Monthly Returns: ')
    print(month_corre_mat)



#(d) Calculate a rolling 90-day correlation of each sector ETF with the S&P index

def roll_corr(df):
    index = df.index
    table = pd.DataFrame(index = index, columns = ['XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'])
    
    for i in range(1,10):
        
        table.iloc[:,i-1] = df['SPY'].rolling(90).corr(df.iloc[:,i])
    
    
    table.plot( title = ' Rolling 90-day correlation of each sector ETF with the S&P index')     
    return table
        

#(e) Use data and a linear regression to calculate the beta. Then list all the historical bate computed by rolling-90 day returns. 

def beta_regression_entire(df):
    
    index = ['β']
    table = pd.DataFrame(index = index, columns = ['XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'])
    X =df['SPY']
    # x =sm.add_constant(X)
    for i in range(1,10):
        Y = df.iloc[:,i]
        Y = pd.DataFrame(Y)
        X = pd.DataFrame(X)
        
        # reg = sm.OLS(Y,X).fit()
        reg = linear_model.LinearRegression().fit(X,Y)
        result = reg.coef_
        table.iloc[:,i-1] =  result[0]
    
    return table


def historical_rolling_beta(df): # I think it's quite complicated to use linear regression to compute rolling beta, so I use cov and variance to compute it.
    
    var_SPY = df['SPY'].rolling(90).var()
    index = df.index
    table = pd.DataFrame(index = index, columns = ['XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'])
    
    for i in range(1,10):
        cov = df['SPY'].rolling(90).cov(df.iloc[:,i])
        beta = cov / var_SPY
        table.iloc[:,i-1] = beta
    
    table.plot(title = 'Rolling-90-day Beta')
    return table
    



#(f) Compute the auto-correlation of each ETF by regressing each ETFs current days return against its previous days returns.

def auto_corr(df):
    
    index = ['α']
    table = pd.DataFrame(index = index, columns = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'])


    for i in range(0,10):
        Y = df.iloc[:,i]
        X = Y.shift(1)
        X = X.fillna(0)
        # X = sm.add_constant(X)
        Y = pd.DataFrame(Y)
        X = pd.DataFrame(X)
        # reg = sm.OLS(Y,X).fit()
        reg = linear_model.LinearRegression().fit(X,Y)
        result = reg.coef_
        table.iloc[:,i] =  result[0]
    
    return table
    

        
        
        
        
    
    





if __name__ == '__main__':
    
    
    stocks = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY']
    source = 'yahoo'
    start_dates = '01-01-2010'
    end_dates = '09-11-2021'
    adj = collect_data(stocks, source, start_dates, end_dates)
    df = returns(adj)
    annual = compute_returns_vol(df)
    print(annual)
    compute_corre_mat(df)
    # Comment:the covariances are higher with monthly returns than daily ones. One possible reason is that the montly returns is the sum of daily returns, which might be higher.
    corr = roll_corr(df)
    
    beta = beta_regression_entire(df)
    print(beta)
    
    rollingbeta = historical_rolling_beta(df)
    
    alpha = auto_corr(df)
    print(alpha)
    

