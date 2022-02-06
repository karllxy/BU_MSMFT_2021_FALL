# 
# homework3-1.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: 1. Sector ETF Factor Modeling
#              
# 

import pandas as pd
import statsmodels.api as sm
from pandas_datareader import data
from sklearn import datasets,linear_model
import numpy as np
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS

# a.  Read, validate and clean data of the Fama-French factors from Ken French’s website.
def collect_factor(filename):
    data = pd.read_csv(filename, index_col = 0)
    data = data/100

    factor = data.sort_index().loc['20100104': '20210730']
    factor = factor.drop(['RF'],axis=1)
    return factor

# b. Calculate the daily covariance matrix of the factor returns over the entire time period
def cov_fmat(factor):
    
    fmat = factor.cov()
    return fmat

# c.Calculate rolling 90 day correlations for the factor returns. 
def roll_fcorr(factor):
    index = factor.index
    table = pd.DataFrame(index = index)
    
    # for i in range(1,len(df.iloc[0,:])):
        
    #     for j in range(1,len(df.iloc[0,:])-i):
            
    #         a =  df.iloc[:,i-1].rolling(90).corr(df.iloc[:,i+j-1]) 
            
    #         table = pd.concat([table,a],axis=1)
            
    
    # # table.columns = ['MKT-RF_SMB','MKT-RF_HML','MKT-RF_RF','SMB_HML','SMB_RF','HML_RF']
    
    table['Mkt-RF_SMB']=factor['Mkt-RF'].rolling(90).corr(factor['SMB']) 
    table['Mkt-RF_HML']=factor['Mkt-RF'].rolling(90).corr(factor['HML'])         
    table['SMB_HML']=factor['SMB'].rolling(90).corr(factor['HML'])      
       
    
    table.plot( title = ' Rolling 90-day correlation of factors with Each Other')     
    return table



# d.Check the factor returns for normality using your favorite test

def check_norm(factor):
    sm.qqplot(factor['Mkt-RF'],line='q')
    sm.qqplot(factor['SMB'],line='q')
    sm.qqplot(factor['HML'],line='q')



# e. linear regression for beta
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

def french_regression(df,factor):
    X = factor
    beta1 = []
    beta2 = []
    beta3 = []
    regr = linear_model.LinearRegression()
    for i in range(len(df.iloc[0,:])):
        Y = df.iloc[:,i]
        result = regr.fit(X,Y)
        param = result.coef_
        # print(param)
        beta1 += [param[0]]
        # print(beta1)
        beta2 += [param[1]]
        beta3 += [param[2]]
    
    table = pd.DataFrame([beta1, beta2, beta3], index = ['β1','β2','β3'],columns = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'])
    return table
        

def rolling_factor_betas(df, factor):
    
    exog_vars = ["Mkt-RF", "SMB", "HML"]
    exog = sm.add_constant(factor[exog_vars])
    exog.index = df.index
    table = pd.DataFrame(index = df.index)
    for i in range(len(df.iloc[0,:])):
        endog = df.iloc[:,i]
        rols = RollingOLS(endog, exog, window=90)
        rres = rols.fit()
        result = rres.params
        table = pd.concat([table,result],join='inner',axis=1)
        
    return table
        
def choose_betas(rolling_factor_betas):
    
    beta1 = pd.DataFrame(index = rolling_factor_betas.index, columns = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'] )
    beta2 = pd.DataFrame(index = rolling_factor_betas.index, columns = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'] )
    beta3 = pd.DataFrame(index = rolling_factor_betas.index, columns = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'] )
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(10):
        beta1.iloc[:,i] = rolling_factor_betas.iloc[:,c1+1]
        c1 = c1+4
    for i in range(10):
        beta2.iloc[:,i] = rolling_factor_betas.iloc[:,c2+2]
        c2 = c2+4
    for i in range(10):
        beta3.iloc[:,i] = rolling_factor_betas.iloc[:,c3+3]
        c3 = c3+4
    return (beta1,beta2,beta3)
        
        
    
# f. Compute the daily residuals ? i,t in (1) for each sector ETF.

def compute_residuals(betas,df,factor):
    table = pd.DataFrame(index = factor.index, columns = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY'] )
    df.index =factor.index
    for i in range(len(betas.iloc[0,:])):
        beta1 = betas.iloc[:,i][0]
        beta2 = betas.iloc[:,i][1]
        beta3 = betas.iloc[:,i][2]
        # print(beta3)
        tablee = beta1 * factor.iloc[:,0] + beta2* factor.iloc[:,1] + beta3 * factor.iloc[:,2]
        # print(tablee)
        table.iloc[:,i] =tablee
    table = df - table
    
    return table
        
        
        
    
        
        
    





if __name__ == '__main__':


    filename = 'F-F_Research_Data_Factors_daily.csv'
    factor = collect_factor(filename)
    fmat = cov_fmat(factor) #much lower than former ETFS, but this doesn't mean they have lower correlation
    froll = roll_fcorr(factor)
    check_norm(factor)
 
 
    stocks = ['SPY','XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY']
    source = 'yahoo'
    start_dates = '01-01-2010'
    end_dates = '07-30-2021'
    adj = collect_data(stocks, source, start_dates, end_dates)
    df = returns(adj)
    #regression betas
    betas = french_regression(df,factor)
    rolling_factor_betas = rolling_factor_betas(df, factor)
    chose_beta = choose_betas(rolling_factor_betas)
    
    #constant?
    chose_beta[0].plot()
    chose_beta[1].plot()
    chose_beta[2].plot()
    
    compute_residual = compute_residuals(betas,df,factor)