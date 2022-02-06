# 
# homework1_2.py - Assignment 5, homework 1
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Build an options strategy that replicates selling a put option using a call option and aposition in the underlying index
# 
#

import opstrat as op
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

'''To replicate Selling a put option, we need to do two things:
The first step is to buy a stock, the second is to sell a call option.'''



def produce_sell_put_opt(S0=100,K=102,C=2):
#this function Assume that initial stock price is 100 ,strike price is 102 and premiun of the option is 2, and we can also change these parameters.

  ST = np.arange(0, S0*2) #list of stock price at expiration of the call

  # Profit of stock position, payoff of Selling call option
  r1 = ST - S0
  r2 = np.where(ST > K, ((K-ST)+ C), C)

  #Total payoff(the strategy payoff)
  r3 = np.where(ST > K,((K-S0)+C),((ST-S0)+C))



  #plot
  fig, ax = plt.subplots()

  ax.spines['top'].set_visible(False) # Top border removed 
  ax.spines['right'].set_visible(False) # Right border removed
  ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
  ax.tick_params(top=False, right=False) # Removes the tick-marks on the RHS

  plt.plot(ST,r1,label='Stock Position')
  plt.plot(ST,r2,label='the Sold Call Option')
  plt.plot(ST,r3,label='the strategy Payoff')

  plt.title('Option Strategy Payoff') 
  plt.xlabel('Prices')
  plt.ylabel('Profit')

  plt.grid(True)
  plt.axis('tight')
  plt.legend(loc=0)
  plt.show()
  
  
  
  
if __name__ == '__main__':
    
    produce_sell_put_opt()
    
    
    
    
    
    
    
    
    