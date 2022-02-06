# 
# homework1.py - Assignment 4 & 5, homework 1
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: 4.Historical Analysis of Sector ETFs
#              5.Build an options strategy that replicates selling a put option using a call option and aposition in the underlying index
# 
#

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pandas_datareader import data

#4.a. Download data for the set of ETFs on yahoo finance and clean as needed

def download_data(stocks, source, start_dates, end_dates):
    
    prices = data.DataReader(stocks, source, start_dates, end_dates)
    
    return prices


#4.b. Compute a table with annualized returns and annualized volatilities for the set of ETFs

def compute_returns_vol(df):
    
    ''' Use the whole data to compute annual return '''    
   
    adj = df['Adj Close']
    total_return = adj.iloc[-1] / adj.iloc[0]
    av_daily_return = total_return **(1/len(adj)) - 1
    annual_return = (1 + av_daily_return) ** 252 - 1

    # print(annual_return)
    # print()
    
    ''' Then compute the annualized volatilities'''
    
    daily_return = df['Adj Close'] / df['Adj Close'].shift(1) - 1
    s = daily_return.std()
    sigma = s * (252**0.5)
    # volatilities = sigma / ((2 * ( len(adj)-1))**0.5)
    
    
    
    # print(volatilities)
    index = annual_return.index
    table = pd.DataFrame(index = index, columns = ['Annualized Returns','Annualized Volatilities'])
    table['Annualized Returns'] = annual_return
    table['Annualized Volatilities'] = sigma
    
    return table

#4.c. Compute a correlation matrix of daily returns for the set of ETFs

def compute_corre_mat(df):
    
    daily_return = df['Adj Close'] / df['Adj Close'].shift(1) - 1
    
    mat = daily_return.corr()
    print(mat)
    
    return mat
    
    
#4.d. Plot the cumulative returns to an investor holding each ETF, as well as an equally weighted portfolio
    
def plot_cum(df):
    daily_return = df['Adj Close'] / df['Adj Close'].shift(1) - 1
    daily_return += 1
    cum_return = daily_return.cumprod()

    cum_return -=  1
    
    co_list = list(cum_return)
    cum_return['Portfolio'] = cum_return[co_list].sum(axis=1)
    cum_return['Portfolio'] = cum_return['Portfolio'] / len(co_list)
    
    cum_return.plot()
    return cum_return
    




##5. Option Strategy

'''To replicate Selling a put option, we need to do two things:
The first step is to buy a stock, the second is to sell a call option.'''

def produce_sell_put_opt(S0=100,K=102,C=2,ranges=200):
    
#this function Assume that initial stock price is 100 ,strike price is 102 and premiun of the option is 2, and we can also change these parameters.

    ST = np.arange(0, ranges) #list of stock price at expiration of the call.

  # Profit of stock position, payoff of Selling call option
    r1 = ST - S0
    r2 = np.where(ST > K, ((K-ST)+ C), C)

  #Total payoff(the strategy payoff)
    r3 = np.where(ST > K,((K-S0)+C),((ST-S0)+C))



  #plot
    fig, ax = plt.subplots()
    plt.plot(ST,r1,label='Stock Position')
    plt.plot(ST,r2,label='the Sold Call Option')
    plt.plot(ST,r3,label='the Strategy Payoff')

    plt.title('Option Strategy Payoff') 
    plt.xlabel('Prices')
    plt.ylabel('Profit')

    plt.grid(True)
    plt.legend(loc=0)
    plt.show()














if __name__ == '__main__':
    
#show the result of assianment 4    
    stocks = ['SPY','DBC','HYG','EEM','MFS=F','AGG','IAGG']
    source = 'yahoo'
    start_dates = '01-01-2018'
    end_dates = '01-01-2021'
    df = download_data(stocks, source, start_dates, end_dates)
    print(compute_returns_vol(df))
    compute_corre_mat(df)
    plot_cum(df)
    
    
# show the result of assianment 5   
    produce_sell_put_opt()
    
    