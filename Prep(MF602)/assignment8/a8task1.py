#
# 87task1.py (Assignment 8, Problem 1)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Simulating Stock Returns
# 
#
import numpy as np
import math
import matplotlib.pyplot as plt

class MCStockSimulator:
    """encapsulates the data and methods required to simulate stock returns and values
    """

# function 1
    def __init__(self, s , t, r, sigma, nper_per_year):
        """ define the basic parameter 
        """
        self.s = s
        self.t = t
        self.r = r
        self.sigma = sigma
        self.nper_per_year = nper_per_year
        
    
    def __repr__(self):
        """This method formats s,t,r,sigma and nper_per_year """
        return f"StockSimulator  (s = ${self.s:0.2f}, t={self.t:6.2f}(year), r= {self.r:6.2f}, sigma= {self.sigma:6.2f}, nper_per_year= {self.nper_per_year:6.2f})"

    
# # function 2    
#     def generate_simulated_stock_returns(self):
#         """generate and return a np.array (numpy array) containing a sequence of simulated stock returns over the time period t
#         """
#         # result = np.zeros(self.t * self.nper_per_year)
        
#         result = []
#         for i in range(self.t , self.nper_per_year + 1):
            
        
        
#             dt = 1 / self.nper_per_year
#             Z = np.random.standard_normal()
            
#             result += [(self.r - self.sigma**2) * dt + Z * self.sigma * (dt**2)]
          
#         return np.array(result)
            
# Function 2
    def generate_simulated_stock_returns(self):
        """Generate and return a np.array (numpy array) 
        containing a sequence of simulated stock returns over the time period t
        """

        output = [] 
        for i in range(0, int(self.t * self.nper_per_year)):
            dt = 1/self.nper_per_year
            Z = np.random.standard_normal()
            simulated_return  = (self.r - (self.sigma ** 2) / 2 )  * dt + Z * self.sigma *(dt ** (0.5))
            output += [simulated_return]
            
        return np.array(output)

# function 3
    def generate_simulated_stock_values(self):
        """ generate and return a np.array (numpy array) containing a sequence of stock values, corresponding to a random sequence of stock return.
        """
        
        returns = self.generate_simulated_stock_returns()
        true_return = math.e ** returns
        result = [self.s]
        price = 0
        for i in range(0, int(self.t * self.nper_per_year)):
            price = result[-1] * true_return[i]
            
            result += [price]
        
        return np.array(result)
            
# function 4    
    def plot_simulated_stock_values(self, num_trials =1):
        """generate a plot of of num_trials series of simulated stock returns. num_trials is an optional parameter; if it is not supplied, the default value of 1 will be used.
        """
        x = np.linspace(0,self.t , self.t * self.nper_per_year +1)

        number = num_trials
        plt.title(str(number) + " simulated_trials")
        plt.xlabel("years")
        plt.ylabel("$ value")
        
        for i in range(num_trials):
            y = self.generate_simulated_stock_values()
            plt.plot(x,y)
            
        plt.show()
            
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    # sim = MCStockSimulator(100, 1, 0.10, 0.30, 2)
    # sim.generate_simulated_stock_returns()
    sim = MCStockSimulator(100, 10, 0.10, 0.30, 24)
    sim.plot_simulated_stock_values()
    
    # sim2 = MCStockSimulator(100, 2, 0.10, 0.30, 250)
    # sim2.plot_simulated_stock_values(5)