#
# a5task2.py (Assignment 5, Problem 2)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  Estimating a Square Root
# 
#

# function 1
def rational_root(n,accuracy):
    """find a fraction that approximates the square root of an integer n to a prescribed degree of accuracy. 
    The function should return a list containing the numerator and denominator of the fraction."""
    
        
    #tring K    
    k = 1
    while k ** 2 <= n :
        print('Tring K = ' +str(k) + ' K**2= ' + str(k **2))
        k += 1
    k = k-1
    
    
    #test whether n is a perfect square number
    if k**2 == n:
        return print(str(n) + ' is a perfect square, with a root of '+str(k)+'.\n'+ str([k,1]))
 
    
    #if n isn't a square number:                 
    print('Using K = ' + str(k)+'\n')
    
    lower_num = k
    lower_denom = 1
    upper_num = k+1
    upper_denom = 1
    mid_num = lower_num + upper_num
    mid_denom = lower_denom + upper_denom
    root = mid_num / mid_denom
   
    while abs(root**2 - n) >= accuracy:
    
        if root**2 < n:
            diff = n - root**2
            print('testing '+str(mid_num)+ '/' +str(mid_denom)+ '. . . diff = '+ format(diff,'.6f') + ' adjust lower bound.')
            lower_num = mid_num
            lower_denom = mid_denom
            mid_num = lower_num + upper_num
            mid_denom = lower_denom + upper_denom
            root = mid_num / mid_denom
        elif root**2 > n:
            diff = n - root**2
            print('testing '+str(mid_num)+ '/' +str(mid_denom)+ '. . . diff = '+ format(diff,'.6f') + ' adjust upper bound.')
            upper_num = mid_num
            upper_denom = mid_denom
            mid_num = lower_num + upper_num
            mid_denom = lower_denom + upper_denom
            root = mid_num / mid_denom
    
    if root**2 < n:
        diff = n - root**2
        print('testing '+str(mid_num)+ '/' +str(mid_denom)+ '. . . diff = '+ format(diff,'.6f') + ' adjust lower bound.')
        
    elif root**2 > n:
        diff = n - root**2
        print('testing '+str(mid_num)+ '/' +str(mid_denom)+ '. . . diff = '+ format(diff,'.6f') + ' adjust upper bound.')
       
    
    print('done.\n')
    print('The Square root of '+ str(n) + ' is approximately '+ str(mid_num)+ '/' +str(mid_denom) + ' = ' + format(root,'.6f'))
    print('The actual square root of '+ str(n)+ ' is ' + format(n**0.5,'.6f'))
    print(str([mid_num,mid_denom]))
            
    
    return [mid_num,mid_denom]
    
    








if __name__ == '__main__':
    
    rational_root(13,0.01)