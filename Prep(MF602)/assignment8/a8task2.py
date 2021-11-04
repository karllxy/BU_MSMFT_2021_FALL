##
# a8task2.py (Assignment 8, Problem 2)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Pricing Path-Dependent Options
# 
#

import math
from a8task1 import MCStockSimulator
import numpy as np

class MCStockOption(MCStockSimulator):
    """This class will encapsulate the idea of a Monte Carlo stock option, and will contain some additional data members( that are not part of class MCStockSimulator and are required to run stock-price simulations and calculate the option’s payoff.
    """
# step 1
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        """The data required include:s (the current stock price in dollars),t (the option maturity time in years),r (the annualized rate of return on this stock),x, which is the option’s exercise pricesigma (the annualized standard deviation of returns),nper_per_year (the number of discrete time periods per year),num_trials, which is the number of trials to run when calculating the value of this option   
        """
        
        super().__init__(s , t, r, sigma, nper_per_year)
        self.x = x
        self.num_trials = num_trials
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCStockOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"
    
    
# step 2 
## method a
    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        print('Base class MCStockOption has no concrete implementation of .value()')
        return 0


## method b
    def stderr(self):
        """return the standard error of this option’s value
        """
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        
        return 0
        

# step 3
class MCEuroCallOption(MCStockOption):
        
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
            
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCEuroCallOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"

    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        
        trials = []
        
        for i in range(self.num_trials):
            
            
            
            slist = self.generate_simulated_stock_values()
            # print(slist)
            st = slist[-1]
            # print(st)
            a = st - self.x
            if a > 0:
                c = (st - self.x) * math.e **(-self.r*self.t)
            elif a <= 0:
                c = 0
            
            trials += [c]

        mean = np.mean(trials)
        stdev = np.std(trials)
        self.mean = mean
        self.stdev = stdev
        return mean
    
# step 4
class MCEuroPutOption(MCStockOption):
        
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
            
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCEuroPutOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"

    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        
        trials = []
        
        for i in range(self.num_trials):
            
            
            
            slist = self.generate_simulated_stock_values()
            # print(slist)
            st = slist[-1]
            # print(st)
            a = self.x -st
            if a > 0:
                c = (self.x - st) * math.e **(-self.r*self.t)
            elif a <= 0:
                c = 0
            
            trials += [c]

        mean = np.mean(trials)
        stdev = np.std(trials)
        self.mean = mean
        self.stdev = stdev
        return mean
            

# step 5
class MCAsianCallOption(MCStockOption):
        
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
            
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCAsianCallOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"

    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        
        trials = []
        
        for i in range(self.num_trials):
            
            
            
            slist = self.generate_simulated_stock_values()
            # print(slist)
            avs = np.mean(slist)
            # print(st)
            a = avs - self.x
            if a > 0:
                c = (avs - self.x) * math.e **(-self.r*self.t)
            elif a <= 0:
                c = 0
            
            trials += [c]

        mean = np.mean(trials)
        stdev = np.std(trials)
        self.mean = mean
        self.stdev = stdev
        return mean
        

# step 6
class MCAsianPutOption(MCStockOption):
        
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
            
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCAsianPutOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"

    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        
        trials = []
        
        for i in range(self.num_trials):
            
            
            
            slist = self.generate_simulated_stock_values()
            # print(slist)
            avs = np.mean(slist)
            # print(st)
            a = self.x -avs
            if a > 0:
                c = ( self.x - avs) * math.e **(-self.r*self.t)
            elif a <= 0:
                c = 0
            
            trials += [c]

        mean = np.mean(trials)
        stdev = np.std(trials)
        self.mean = mean
        self.stdev = stdev
        return mean

# step 7
class MCLookbackCallOption(MCStockOption):
        
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
            
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCLookbackCallOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"

    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        
        trials = []
        
        for i in range(self.num_trials):
            
            
            
            slist = self.generate_simulated_stock_values()
            # print(slist)
            maxs = np.max(slist)
            # print(st)
            a = maxs - self.x
            if a > 0:
                c = (maxs - self.x) * math.e **(-self.r*self.t)
            elif a <= 0:
                c = 0
            
            trials += [c]

        mean = np.mean(trials)
        stdev = np.std(trials)
        self.mean = mean
        self.stdev = stdev
        return mean


# step 8 
class MCLookbackPutOption(MCStockOption):
        
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
            
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)
        
        
    def __repr__(self):
        """ create a nicely formatted printout of the MCStockOption object, which will be useful for debugging your work.
        """
        return f"MCLookbackPutOption, s = ${self.s:0.2f}, x={self.x:6.2f}, t={self.t:6.2f}, r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f}, num_trials={self.num_trials:4.0f}"

    def value(self):
        """return the value of the option. This method cannot be concretely implemented in this base class, but will be overridden in each subclass (see below). 
        """
        
        trials = []
        
        for i in range(self.num_trials):
            
            
            
            slist = self.generate_simulated_stock_values()
            # print(slist)
            mins = np.min(slist)
            # print(st)
            a = self.x -mins
            if a > 0:
                c = ( self.x - mins) * math.e **(-self.r*self.t)
            elif a <= 0:
                c = 0
            
            trials += [c]

        mean = np.mean(trials)
        stdev = np.std(trials)
        self.mean = mean
        self.stdev = stdev
        return mean



if __name__ == '__main__':
    # call = MCEuroCallOption(90, 100, 1, 0.1, 0.3, 100, 1000)
    # print(call)
    # call.value()
    
    
    # bs_call = BSEuroCallOption(40, 40, 0.25, 0.3, 0.08)
    # bs_call.value()

    # call = MCEuroCallOption(90, 100, 1, 0.1, 0.3, 100, 1000)
    # print(call)
    # put = MCEuroPutOption(100, 100, 1.0, 0.1, 0.3, 100, 1000)
    # print(put)
    
    acall = MCAsianCallOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    print(acall)
    
    # aput = MCAsianPutOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    # print(aput)
    
    # lcall = MCLookbackCallOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    # print(lcall)
    
    # lput = MCLookbackPutOption(100,100,1.0,0.10,0.30,100,1000)
    # print(lput)

    
    
    