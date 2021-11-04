# 
# a2task1.py - Assignment 2, Task 1
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Decision Statements
# 
#

# function 1
def smaller(x,y):
    """this function takes two numbers x and y 
    and returns the smaller of the two numbers.
    """
    if x < y:
        return x
    if x >= y:
        return y
    
    
# function 2
def smallest(x,y,z):
    """takes three parameters and returns the smallest of the three.
    x,y,z could be any number.
    """
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z


# function 3
def is_factor(n,x):
    """This function takes a two integers n and x, and 
    returns True if x is a factor of n and False otherwise.
    """
    if n % x == 0:
        return True
    else:
            return False


# function 4
def has_vowel(s):
    """this function takes a string s and returns True 
    if the string contains at least one vowel (any letter in 'aeiou') 
    and False otherwise.
    """
    if 'a' in s:
        return True
    if 'e' in s:
        return True
    if 'i' in s:
        return True
    if 'o' in s:
        return True
    if 'u' in s:
        return True
    # if 'a' or 'e' or 'i' or 'o' or 'u' in s:
    else:
        return False
    
    






# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':
    
    print('smaller(20,4)',smaller(20,4))
    print('smaller(5,8)',smaller(5,8))
    print('smallest(20,4,17)',smallest(20,4,17))
    print('smallest(10,8,4)',smallest(10,8,4))
    print('smallest(10,8,10)',smallest(10,8,10))
    print('smallest(10,18,10)',smallest(10,18,10))
    print('is_factor(20,4)',is_factor(20,4))
    print('is_factor(4321,13)',is_factor(4321,13))
    print('is_factor(5338,17)',is_factor(5338,17))
    print('has_vowel(''finance'')',has_vowel('finance'))
    print('has_vowel(''czyk'')',has_vowel('czyk'))

