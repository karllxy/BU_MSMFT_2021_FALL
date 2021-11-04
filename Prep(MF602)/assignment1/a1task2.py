# 
# a1task2.py - Assignment 1, Task 2
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Functions with numeric inputs
# 
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

#function 1
def cube(x):
    """returns the cube of its 
    input (i.e., x raised to the power of 3)
    
    """
    return x**3

#function 2
def slope(x1,y1,x2,y2):
    """retunrs the slope of two points in the Cartesian plane
    input x1,x2,y1,y2: any number (int or float)
    
    """
    return (y2 - y1) / (x2 - x1)

#function 3
import math
def cylinder_volume(diameter, height):
    """returns the volume of a cylinder of a given diameter and height
    input diameter and height : any number (int or float)
    """
    return math.pi * height * (diameter / 2) ** 2

    







# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':

    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))

    # add test calls for your functions below
    print('cube(-5) returns',cube(-5) )
    print('slope(2,3,5,3) returns', slope(2,3,5,3))
    print('cylinder_volume(10,10)',cylinder_volume(10,10))
    print('cylinder_volume(20,10)',cylinder_volume(20,10))
    
