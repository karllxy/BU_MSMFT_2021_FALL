# 
# a3task1.py - Assignment 3, Task 1
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Descriptive Statistics
# 
#

# function 1
def mean(values):
    """ this function takes as a parameter a list of numbers, and calculates 
    and returns the mean of those values
    """
    summa = 0
    for i in values:
        summa += i
    return summa / len(values)


# function 2
def variance(values):
    """returns the population variance of the values in a list"""
    summa = 0
    for i in values:
        summa +=( i - mean(values)) ** 2
    return summa / len(values)


# function 3
def stdev(values):
    """this function returns the population standard deviation of the values in given list"""
    return variance(values) **0.5


# function 4
def covariance(x,y) :
    """returns the population covariance for those two lists."""
    summa = 0
    if len(x) != len(y):
        return 'Error! The lenth of two lists are not same.'
    else:
        for i in range(0,len(x)):
            summa += (x[i] - mean(x)) * (y[i] - mean(y))
        return summa / len(x)


# function 5        
def correlation(x,y):
    """returns the correlation coefficient between these data series."""
    if len(x) != len(y):
        return 'Error! The lenth of two lists are not same.'  
    else:
        return covariance(x,y) / (stdev(x) * stdev(y))
    

# function 6
def rsq(x,y):
    """returns the square of the correlation between those two data series, 
    which is a measure of the goodness of fit measure to explain variation in y as a function of variation of x.
    """
    return correlation(x,y) ** 2

# function 7
def simple_regression(x,y):
    """ returns the regression coefficients between these data series.
    """
    beta = covariance(x,y) / variance(x)
    alpha = mean(y) - beta * mean(x)
    return (alpha,beta)




if __name__ == '__main__':
    
    print(mean([4,4,3,6,7]))
    print(variance([4,4,3,6,7]))
    print(stdev([4,4,3,6,7]))
    x=[4,4,3,6,7]
    y=[6,7,5,10,12]
    print(covariance(x,y))
    print(correlation(x,y))
    print(rsq(x,y))
    print(simple_regression(x,y))