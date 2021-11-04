#
# a6task3.py (Assignment 6, Problem 3)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  Matrix Application: Bond Pricing
# 
#
from a4task1 import discount_factors, bond_cashflows
from a6task1 import *
from a6task2 import *
# function 1
def bond_price(fv,c,n,m,r):
    """calculate and return the price of a bond
    """
    bond_cf_matrix = [bond_cashflows(fv,c,n,m)]
    discount_factors_matrix = [discount_factors(r,n,m)]
    price = dot_product(discount_factors_matrix, transpose(bond_cf_matrix))
    
    return price[0][0]



# fuhnction 2
def bootstrap(cashflows,prices):
    """This function will take parameters cashflows, which is a matrix (2-dimensional list) containing the cashflows for some bonds, and prices which is a column matrix (2-dimensional list) containing the prices of these bonds
    """
    inverse_cashflows = inverse_matrix(cashflows)
    
    r = dot_product(inverse_cashflows, prices)
    
    return r



















if __name__ == '__main__':
    bond_price(1000, 0.08, 5, 2, 0.08)
    
    CF = [[105,0,0],[6,106,0],[7,7,107]]
    P = [[99.5], [101.25], [100.35]]
    D = bootstrap(CF, P)
    print_matrix(CF, 'Bond Cashflows')

    print_matrix(P, 'Bond Prices')


    print_matrix(D, 'Implied Discount Factors') 



    
