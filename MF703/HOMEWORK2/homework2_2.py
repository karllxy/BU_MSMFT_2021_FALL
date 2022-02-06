# 
# homework2-2.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: 2. Exotic Option Pricing via Simulation
#              
# 
import numpy as np
import math
import matplotlib.pyplot as plt
import statistics
import pandas as pd
import scipy.stats as si

# (a) Generate a series of normally distributed random numbers and use these to generate simulated paths for the underlying asset

def generate_path_asset(T = 1, nper_per_year = 365, trials = 1000, sigma = 0.25, r = 0):#nper_per_year is the number of discrete time periods per yea
    
    S0 = 100

    dt = 1 / nper_per_year
    S_all = []
    S_term = []
    for i in range(0,trials):
        
        S = [S0]
    
        for j in range(0, nper_per_year):
            dw = np.random.normal(0, dt**0.5) 
            S  += [S[-1] * (1+ r * dt + sigma * dw)]
        S_all  += [S]   
        S_term += [S[-1]]
        
    return (S_term, S_all)


# (b) Calculate the payoff of a European put option with strike 100 along all simulated paths.

def Europ_put_payoff(paths):
    
    trials = []
    x = 100   
    for i in range(len(paths[0])):
            
            
            
        st = paths[0][i][-1]
            # print(st)
        a = x -st
        if a > 0:
            c = (x - st) 
        elif a <= 0:
            c = 0
            
        trials += [c]
    
    return trials


# (c) Calculate a simulation approximation to the price of a European put option by taking the average discounted payoff across all paths.
def discounted_price(payoff, r = 0, T = 1):
    
    dis_price = pd.DataFrame(payoff)
    dis_price = dis_price * math.exp(-r * T)
    dis_price = dis_price.mean()
    return dis_price
    

# (d)  Compare the price of the European put option obtained via simulation to the price you obtain using the Black-Scholes formula.
def BS_put_price(S0 = 100, K = 100, T = 1, r = 0, sigma = 0.25):
    
    d1 = (math.log(S0/K) + (r + 0.5 * (sigma **2)) *T)  / (sigma * (T** 0.5))
    d2 = d1 - (sigma * (T ** 0.5))
    
    price = K * (1 - si.norm.cdf(d2)) - S0 * (1 - si.norm.cdf(d1))
    
    return price



# (e) Calculate the payoff of a fixed strike lookback put option with stike 100 along all simulated path. 

def lookback_payoff(paths, K=100, r = 0 , t = 1):
    
    min_price = pd.DataFrame(paths[0]).T.min() # might be quite complex while r =! 0
    
    
    lookback_payoff = K - min_price
    disc_lookback_payoff = lookback_payoff.mean()
    
    return lookback_payoff, disc_lookback_payoff
    

# (f)Calculate the premium that the buyer is charged for the extra optionality embedded in the lookback.

def difference(look_back, dis_price):
    
    return look_back[1] - dis_price


# (g) Try a few different values of σ and comment on what happens to the price of the European, the Lookback option and the spread/premium between the two.

def change():
    
    sigma_list = np.arange(0,1,0.05)
    dis_lst = []
    lookback_lst =[]
    diff_lst = []
    for i in range(len(sigma_list)):
       Sigma = sigma_list[i]
       glst = generate_path_asset(T = 1, nper_per_year = 365, trials = 100, sigma = Sigma)
       paths = [glst[1]]
       payoff1 = Europ_put_payoff(paths)
       dis_price = discounted_price(payoff1)
       look_back = lookback_payoff(paths)
       diff = difference(look_back, dis_price)
       
       dis_lst += [dis_price[0]]
       lookback_lst += [look_back[1]]
       diff_lst += [diff[0]]
       
    
    lst = [sigma_list, dis_lst, lookback_lst, diff_lst]
    lst_ = pd.DataFrame(lst).T
    lst_.columns = ['Sigma', 'European Put Option Payoffs', 'Lookback Option Payoffs', 'the Difference']
    lst_.set_index(['Sigma'],inplace = True)
    lst_.plot(title = 'the Payoffs with Increasing Sigma')
    return lst_
    
       
       
    







if __name__ == '__main__':
    
    
    lst = generate_path_asset()
    paths = [lst[1]]
    payoff1 = Europ_put_payoff(paths)
    plt.hist(payoff1)
    
    meanp = statistics.mean(payoff1)
    stdv = statistics.stdev(payoff1)
    
    dis_price = discounted_price(payoff1)
   
    # print(dis_price)
    equ_price = BS_put_price()
    # print(equ_price)
    diff_BS_EUR = statistics.mean(payoff1) - equ_price
    print('the difference between simulation and BS model in this round is: ' + str(diff_BS_EUR))
    look_back = lookback_payoff(paths)
    print('the lookback option price is about: ' + str(look_back[1]))
    diff = difference(look_back, dis_price)
    print('the premium of the lookback option is about: ' + str(diff[0])) #seems never become negative
    
    result = change() # show the relation between sigma and diff
    
    
    
    
    
    
        
        
        