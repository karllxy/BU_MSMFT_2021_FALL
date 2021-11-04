#
# a9task2.py (Assignment 9, Problem 2)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  Calculating Drawdown
# 
#
import pandas as pd
from a9task1 import *
from a8task1 import MCStockSimulator
import numpy as np

# function 1
def compute_drawdown(prices):
    """The function returns a pandas.DataFrame object containing these columns:
price, which is a copy of the data in the parameter prices
prev_max, which contains the previous peak price before this price,
dd_dollars, which is the drawdown since the previous maximum price, measured in dollars,
dd_pct, which is the percentage decline since the previous maximum price
    """

    index = prices.index
    df = pd.DataFrame(index = index, columns = ['price', 'prev_max', 'dd_dollars','dd_pct'])
  
    
   
    df['price'] = prices.iloc[:,0]
    
    prev_max = prices.iloc[:,0]
    # print(prev_max)
    for i in range(1,len(prev_max)):
        if prev_max[i] <= prev_max[i-1]:
            prev_max[i] = prev_max[i-1]  
    # print(prev_max)
    # print(pricelist)
    dd_dollars = prev_max - df['price']
    # print(dd_dollars)
    dd_pct = dd_dollars / prev_max   
    
    # df['price'] = pricelist
    
    df['prev_max'] = prev_max
    df['dd_dollars'] = dd_dollars
    df['dd_pct'] = dd_pct
        
    return df
    

# function 2
def plot_drawdown(df):
    """The parameter df, is a pandas.DataFrame object containing these columns:
price, which is a copy of the data in the parameter prices
prev_max, which contains the previous peak price before this price
dd_dollars, which is the drawdown since the previous maximum price, measured in dollars
dd_pct, which is the percentage decline since the previous maximum price
    """
    index = df.index
    df2 = pd.DataFrame(index = index, columns = ['price', 'prev_max'])
    
    df2['price'] = df['price']
    df2['prev_max'] = df['prev_max']
    
    
    df2.plot(title = 'Price and Previous Maximum')
    
    index = df.index
    df3 = pd.DataFrame(index = index, columns = ['dd_pct'])
    
    df3['dd_pct'] = df['dd_pct']
    
    
    
    df3.plot(title = 'Drawdown Percentge')
    
    

# function 3
def run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials):
    """use the MCStockSimulator from assignment 9 to run num_trials using MC simulations, and calculate the maximum drawdown for each trial.
    """
    sim = MCStockSimulator(init_price, years, r, sigma, trial_size)
    
    
    
    lst = []
    maxnum = 0
    for i in range(num_trials):
        
        simlist = sim.generate_simulated_stock_values()
        df = pd.DataFrame(simlist)
    
        dd = compute_drawdown(df)
    
        maxnum = dd['dd_pct'].max()
    
        lst  += [maxnum]
        
    result = pd.Series( data = lst)
    
    return result
    
    

    


















if __name__ == '__main__':
    df = pd.read_csv('AAPL.csv')
    # # set the 'Date' column as index
    # df.index = df['Date']
    # prices = pd.DataFrame(df.loc['2017-01-01':'2017-12-31','Adj Close'])
    # # compute drawdown for this one stock
    # dd = compute_drawdown(prices)
    # plot_drawdown(dd)
    
    df['ret'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))    
    trial_size = 252 # trading days/year
    init_price = float(df['Adj Close'].sample())
    r = df['ret'].mean() * trial_size
    sigma = df['ret'].std() * np.sqrt(trial_size)
    years = 10
    num_trials = 100
    max_dd = run_mc_drawdown_trials(init_price,  years, r, sigma, trial_size, num_trials)
