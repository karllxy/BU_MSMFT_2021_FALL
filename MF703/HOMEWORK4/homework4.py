# 
# homework4.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Volatility Experiments
#              
# 
import math
import pandas as pd
import statsmodels.api as sm
from pandas_datareader import data
from sklearn import datasets,linear_model
import numpy as np
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS
from pyspark.sql.functions import col, log
import scipy.stats as si
import matplotlib.pyplot as plt
from scipy import stats

#(a) Download historical data for the S&P using the SPY ETF and for the VIX index, which we will use as a proxy for volatility.
def collect_data(stocks, source, start_dates, end_dates):
    Data = data.DataReader(stocks, source, start_dates, end_dates)
    adj = Data['Adj Close']
    
    condition = adj.isnull().any()
    


    for i in range(len(adj.iloc[0,0:])): #  Use 'if' sentence to check whether each line lose data or not
        
        if condition[i] == True:
            adj.iloc[:,i] = adj.iloc[:,i].fillna( method='ffill') # Here I assume that there weren't be a large amount NAN data in these ETFs, so I use former data to fill NAN if possible.
    
    return adj


def returns(adj):     
    
    #df = adj.pct_change()[1:]
    df = pd.DataFrame(index=adj.index)
    df['SPY'] = adj['SPY'] / adj['SPY'].shift(1) - 1 
    df = df.iloc[1:] # The first raw of df would be NAN since there's no more data to calculate its returns, so I just drop it.
    df['^VIX'] = adj['^VIX'][1:]/100
    
    return df



#(b) Examine both the S&P and the VIX index data for autocorrelation
def auto_corr(df):
    
    r = []
    t = []
    for i in range(0,2):
        Y = df.iloc[:,i]
        X = Y.shift(1)
        X = X.fillna(0)
        X = sm.add_constant(X)
        # Y = pd.DataFrame(Y)
        # X = pd.DataFrame(X)
        reg = sm.OLS(Y,X).fit()
        # reg = linear_model.LinearRegression().fit(X,Y)
        result = reg.params
        tvalues = reg.tvalues
        print(reg.summary())
        r += ([result])
        t += [tvalues]
        
    
    return (r,t)


#(c)Calculate the correlation of the S&P and its implied volatility (using VIX as a proxy) on a daily and monthly basis.

def daily_corr(df):
    
    table = stats.pearsonr(df["SPY"],df["^VIX"])
    return table

def month_return(df):
    # logreturn = pd.DataFrame(index=df.index)
    
    # logreturn['SPY'] = df['SPY'].apply(np.log1p)
    # logreturn['^VIX'] = df['^VIX']
    # logreturn = logreturn.resample('M').sum()
    # monthreturn = pd.DataFrame(index=logreturn.index)
    # monthreturn['SPY'] = logreturn['SPY'].apply(np.expm1)
    # monthreturn['^VIX'] = logreturn['^VIX']
    
    # table = stats.pearsonr(monthreturn ["SPY"],monthreturn["^VIX"])
    vixm  = df['^VIX'].resample('M').last()
    logreturn = df['SPY'].apply(np.log1p)
    logreturn = logreturn.resample('M').sum()
    monthreturn = logreturn.apply(np.expm1)
    month = pd.DataFrame(index=logreturn.index)
    month['SPY'] = monthreturn
    month['^VIX']= vixm
    table = stats.pearsonr(month["SPY"],month["^VIX"])
    return table

    
#(d) Calculate rolling 90-day correlatons of the S&P and its implied volatility
def roll_corr(df):
    index = df.index
    table = pd.DataFrame(index = index) 
    table['SPY_VIX']=df['SPY'].rolling(90).corr(df['^VIX']) 
    mean = table['SPY_VIX'].mean()
    table['Long-run average'] = table['SPY_VIX']/table['SPY_VIX'] * mean
    
    return table


#(e)Calculate rolling 90-day realized volatilities in the S&P and compare them to the implied volatility (again using VIX as a proxy)
def roll_vol(df):
    
    sp2 = pd.DataFrame(index=df.index)
    sp2['realized'] = df['SPY'].rolling(90).std()
    # sp2 = sp2**0.5
    sp2['implied'] = df['^VIX']/(252**0.5)
    
    sp2['premium'] = sp2['implied'] - sp2['realized']

    return sp2
    

#（f) Construct a portfolio that buys a 1M at-the-money straddle everyday. Use the BlackScholes model to compute the option prices and use the level of VIX as the implied vol input into the BS formula. 
def straddle_price(adj, T=1/12, r=0):
    st = adj['SPY']
    k = st
    sigma = adj['^VIX'] /100
    logs = (st/k).apply(np.log)

    d1 = (logs+(r+0.5*(sigma**2))*T)/(sigma * (T ** 0.5))
    d2 = d1 - sigma * (T ** 0.5)
    
    c = st * si.norm.cdf(d1) - k * (math.e**(-r*T)) * si.norm.cdf(d2)
    p = k * (1 - si.norm.cdf(d2)) * (math.e**(-r*T)) - st * (1 - si.norm.cdf(d1))
    price = p + c
    return price


# (g)Calculate the payoffs of these 1M straddles at expiry (assuming they were held toexpiry without any rebalances) by looking at the historical 1M changes in the S&P. Calculate and plot the P&L as well.    

def straddle_payoffs(adj):
    s0 = adj['SPY']
    pwp = []
    for i in range(len(s0)-21):
        k = s0[i]
        st = s0[i+21]
        # if st - k >=0:
        #     cp = st - k
        # else:
        #     cp = 0
        
        # if k - st >=0:
        #     pp = k - st
        # else:
        #     pp = 0
        dpay = abs(st - k)    
        # dpay = pp + cp
        pwp += [dpay]
  

    return pwp
        
def PL(payoff,price):
    
    p = pd.DataFrame( index = price.index[:-21])
    p['payoff'] = payoff
    p['price'] = price[:-21]
    pl = p['payoff'] - p['price']
    
    
        
    
    return pl
          
    
# (h)Make a scatter plot of this P&L against the premium between implied and realized volatility
def prem(roll_vol, pl, df): 
    vix = df['^VIX'][:-21]/(252**0.5)
    real = roll_vol[:-21]
    pre = vix - real
    pl= pl[1:]
    plt.scatter(pl,pre)
    
    return pre
    
    
    







if __name__ == '__main__':
    stocks = ['SPY','^VIX']
    source = 'yahoo'
    start_dates = '01-01-2010'
    end_dates = '07-30-2021'
    adj = collect_data(stocks, source, start_dates, end_dates)
    df = returns(adj)
    
    alpha = auto_corr(df)
    dailycorr = daily_corr(df)
    monthlycorr = month_return(df)
    roll_corr = roll_corr(df)
    roll_vol = roll_vol(df)
    
    price = straddle_price(adj)
    payoff = straddle_payoffs(adj)
    pl = PL(payoff, price)
    prem(roll_vol['realized'], pl, df)
    
    
    
    