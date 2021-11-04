# 
# a2task2.py - Assignment 2, Task 2
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Fun with recursion
# 
#


# function 1
def mult(n,m):
    """return the product of those integers"""
    if m == 0:
        return 0
    elif n < 0:
        return -mult(-n, m)
    else: 
        mult_rest = mult(n, m-1)
        return n + mult_rest


# function 2
def copy(s,n):
    """return a string in which n copies of s have been concatenated together.
    """
    if n <= 0:
        return ''
    else:
        copy_rest = copy(s,n-1)
        return copy_rest + s
    
# function 3
def double(s):
    """takes an arbitrary string s as input, return the string formed by doubling each character in the string.
    """
    if s == '':
        return ''
    else:
        double_rest = double(s[1:])
        return 2 * s[0] + double_rest
    
# fucntion 4
def dot(l1,l2):
    """this function will compute and return the dot product of those lists
    """
    if l1 == [] or l2 == [] or len(l1) != len(l2):
        return 0.0
    else:
        l1_rest = l1[1:]
        l2_rest = l2[1:]
        return l1[0] * l2[0] + dot(l1_rest, l2_rest)
    
# function 5
def find_min(items): 
    """ this function could find the minimum from a list of items.
    """
    if len(items) == 1:
        return items[0]
    else:
        find_rest = find_min(items[1:])
        if items[0] < find_rest:
            return items[0]
        else:
            return find_rest
        

# function 6
def weave(s1, s2):
    """a new string that is formed by “weaving” together the characters
    in the strings s1 and s2 to create a single string.
    """  
    if s1 == '' and s2 == '':
        return ''
    if s1 == '':
        return s2
    if s2 == '':
        return s1
    else:
        s1_rest = s1[1:]
        s2_rest = s2[1:]
    
        return s1[0] + s2[0] + weave(s1_rest, s2_rest)
    
    
    
    










# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':
   
    """ test function for the functions above """
    test1 = mult(6,7)
    print('the first test returns', test1)
    
    test2 = copy('Go BU!',4)
    print('the second test returns', test2)
    
    test3 = double('python')
    print('the thrid test returns ', test3)
    
    test4 = dot ([1,2,3,4],[10,100,1000,10000])
    print('the fouth test returns ',test4)
    
    test5 = find_min(['z','h','e','l','m','c','s'])
    print('the fifth test returns', test5)
    
    test6 = weave('aaaaaa','bb')
    print('the sixth test returns',test6)
    
    
    

   