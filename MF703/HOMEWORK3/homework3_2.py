# 
# homework3-2.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  2. Exotic Option Pricing via Simulation
#              
# 
import numpy as np
import math
import matplotlib.pyplot as plt
import statistics
import pandas as pd
import scipy.stats as si
import statsmodels.api as sm


# a.Generate a series of normally distributed random numbers and use these to generate simulated paths for the underlying asset.
def generate_path_asset(S0 = 100,T = 1, nper_per_year = 365, trials = 100, sigma = 25, r = 0):#nper_per_year is the number of discrete time periods per yea
    


    dt = 1 / nper_per_year
    S_all = []
    S_term = []
    for i in range(0,trials):
        
        S = [S0]
    
        for j in range(0, nper_per_year):
            dw = np.random.normal(0, dt**0.5) 
            S  += [S[-1] + r * dt + sigma * dw]
        S_all  += [S]   
        S_term += [S[-1]]
        
    return (S_term, S_all)

# b. Plot a histogram of the ending values of the asset price along the simulated paths and check normality.
# the solution is below.



# c.Calculate a simulation approximation to the price of a Lookback put option with strike 100 under the Bachelier model.
def lookback_payoff(paths, K=100, r = 0 , t = 1):
    
    min_price = pd.DataFrame(paths[0]).T.min() # might be quite complex while r =! 0
    
    
    lookback_payoff = K - min_price
    disc_lookback_payoff = lookback_payoff.mean()
    
    return lookback_payoff, disc_lookback_payoff

    
# d.Calculate the delta of the lookback option using finite differences as discussed in class.
def deltas(e = 2):
    
    delta = []
    
    for i in np.arange(0,e,0.01):
        
        p1 = generate_path_asset(S0=100 + i, T = 1, nper_per_year = 365, trials = 1000, sigma = 10, r = 0)
        paths1 =  [p1[1]]
        look1 = lookback_payoff(paths1, K=100, r = 0 , t = 1)
        
        p2 = generate_path_asset(S0=100 - i, T = 1, nper_per_year = 365, trials = 1000, sigma = 10, r = 0)
        paths2 =  [p2[1]]
        look2 = lookback_payoff(paths2, K=100, r = 0 , t = 1)
        
        delta += [(look1[1] - look2[1]) / (2 * i)]
    
    return delta
        
        
    
    








if __name__ == '__main__':
    
    
    lst = generate_path_asset()
    paths = [lst[1]]
    terms = lst[0]
    #b. solve
    plt.hist(terms)
    # sm.qqplot(np.array(terms))
    
    look_back = lookback_payoff(paths)
    print('the lookback option price is about: ' + str(look_back[1]))
    dt = deltas(e = 2)
    print(dt)
    x = np.arange(0,2,0.01)
    result = pd.DataFrame(dt,x)
    result.index.name = 'ε'
    result.plot()