# 
# homework6-1.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: 1.Covariance Matrix Decomposition
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



# (a).Download historical price data from January 1st 2010 until today for the sector ETFs in the table above. Clean the data for splits and any other anomalies.

def collect_data(stocks, source, start_dates, end_dates):
    
    Data = data.DataReader(stocks, source, start_dates, end_dates)
    adj = Data['Adj Close']
    
    condition = adj.isnull().any()
    


    for i in range(len(adj.iloc[0,0:])): #  Use 'if' sentence to check whether each line lose data or not
        
        if condition[i] == True:
            adj.iloc[:,i] = adj.iloc[:,i].fillna( method='ffill') # Here I assume that there weren't be a large amount NAN data in these ETFs, so I use former data to fill NAN if possible.
    
    return adj


def returns(adj):     
    
    df = np.log(adj.pct_change()+1)
    df = df.dropna()# The first raw of df would be NAN since there's no more data to calculate its returns, so I just drop it.
    
    return df 


# (b) Calculate the covariance matrix of daily returns for the sector ETFs.

def covmat(df):
    return df.cov()

# (c) Perform an eigenvalue decomposition of the covariance matrix.
def eigen(covmat):
    
    eigenvalue, eigenvector = np.linalg.eig(covmat)
    
    print('The eigenvalues are:' )
    print(eigenvalue)
    rank = np.sort(eigenvalue)
    rank = rank[::-1]
    plt.plot(rank)
    
    


# (d)Generate a random matrix of the same size as your covariance matrix, where each element has a standard normal distribution.

def randmat():
    
    return np.matrix(np.random.normal(size=(9, 9)))



# (e) Perform an eigenvalue decomposition of this random matrix. Plot the eigenevalues in order from largest to smallest










if __name__ == '__main__':
    
    stocks = ['XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY']
    source = 'yahoo'
    start_dates = '01-01-2010'
    end_dates = '07-12-2021'
    adj = collect_data(stocks, source, start_dates, end_dates)
    df = returns(adj)
    covmat = covmat(df)
    eigen(covmat)
    randmat = randmat()
    eigen(randmat)
    