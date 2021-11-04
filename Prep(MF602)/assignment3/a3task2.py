# 
# a3task2.py - Assignment 3, Task 2
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Stock Returns and Statistics
# 
#

# function 1
def calc_returns(prices):
    """This function will process a list of stock prices and calculate the periodic returns"""
    ret = []
    for i in range(1,len(prices)):
        ret += [((prices[i] /prices[i-1]) -1)]
    return ret


# function 2
def process_stock_prices_csv(filename):
    """This function will process a data file containing stock price data, and return a list of stock prices."""
    f = open(filename,'r')
   # count = 0
    empty_list = []
    for line in f.readlines()[1:]:
        fields = line.split(',')
        Adj_close = float(fields[-2])
        empty_list += [Adj_close]
       
    f.close()
    return empty_list


# function 3
from a3task1 import *

def stock_report(filenames):
    """
    the function must return a string containing the entire report, i.e., several outputs, neatly formatted, etc.
    """
    symbol = []
    Mean = []
    Stdev = []
    covar = []
    correl = []
    R_SQ = []
    beta = []
    alpha = []
    p_spy = process_stock_prices_csv(filenames[3])
    returns_spy = calc_returns(p_spy)
    for i in range(0,len(filenames)):
        prices_stock = process_stock_prices_csv(filenames[i])
        returns_stock = calc_returns(prices_stock)
        Mean += [mean(returns_stock)]
        Stdev += [stdev(returns_stock)]
        covar += [covariance(returns_stock,returns_spy)]
        correl += [correlation(returns_stock,returns_spy)]
        R_SQ += [rsq(returns_stock,returns_spy)]
        beta += [simple_regression(returns_stock,returns_spy)[1]]
        alpha += [simple_regression(returns_stock,returns_spy)[0]]
        symbol += [filenames[i][2:-4]]
    table=(f"Calculate returns for 4 stocks. \n\nDescriptive statistics for daily stock returns:\n"
             +f"{'Symbol':10} {symbol[0]:10} {symbol[1]:10} {symbol[2]:10} {symbol[3]:10}\n"
             +f"Means: {Mean[0]:10.5f} {Mean[1]:10.5f} {Mean[2]:10.5f} {Mean[3]:10.5f}\n"
             +f"StDev: {Stdev[0]:10.5f} {Stdev[1]:10.5f} {Stdev[2]:10.5f} {Stdev[3]:10.5f}\n"
             +f"Covar: {covar[0]:10.5f} {covar[1]:10.5f} {covar[2]:10.5f} {covar[3]:10.5f}\n"
             +f"Correl: {correl[0]:9.5f} {correl[1]:10.5f} {correl[2]:10.5f} {correl[3]:10.5f}\n"
             +f"R-SQ: {R_SQ[0]:11.5f} {R_SQ[1]:10.5f} {R_SQ[2]:10.5f} {R_SQ[3]:10.5f}\n"
             +f"Beta: {beta[0]:11.5f} {beta[1]:10.5f} {beta[2]:10.5f} {beta[3]:10.5f}\n"
             +f"Alpha: {alpha[0]:10.5f} {alpha[1]:10.5f} {alpha[2]:10.5f} {alpha[3]:10.5f}\n")
    
    return table
   
        
    
    






if __name__ == '__main__':
    
    prices = [100,110,105,112,115]
    print(calc_returns(prices))
    filenames = ['./AAPL.CSV','./BAC.CSV','./GOOG.CSV','./SPY.CSV']
    print(stock_report(filenames))
