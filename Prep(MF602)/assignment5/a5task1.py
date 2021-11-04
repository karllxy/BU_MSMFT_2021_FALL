#
# a5task1.py (Assignment 5, Problem 1)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Estimating pi using Monte Carlo simulation
# 
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 1 BELOW. ###

# function 1
def for_pi(n):
    """returns an estimate of π that is based on n randomly thrown darts."""
    dart0 = 0
    dart1 = 0
    p = 0
    for i in range(n):
        dart1 += 1
    
        if throw_dart() == True:
            dart0 += 1
        print(str(dart0)+ ' hits of '+ str(dart1) +' throw so that pi is ' + str(4 * dart0 / dart1))
        p = 4 * dart0 / dart1
        
            
    return p


# function 2
def while_pi(error):
    """returns the number of dart throws needed to produce an estimate of π that is less than error away from the “actual” value of π (i.e., the value given by math.pi in Python’s math module)."""
    dart0 = 0
    dart1 = 0
    p_sim = 0
    while abs(p_sim - math.pi) > error:
        dart1 += 1
        
        if throw_dart() == True:
            dart0 += 1
        p_sim = 4 * dart0 / dart1   
        print(str(dart0)+ ' hits of '+ str(dart1) +' throw so that pi is ' + str(p_sim))
    
    print(str(dart1))
    return dart1



if __name__ == '__main__':
    print(for_pi(100))
    while_pi(0.01)