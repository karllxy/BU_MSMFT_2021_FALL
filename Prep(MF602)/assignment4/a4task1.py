# 
# a4task1.py - Assignment 4, Task 1
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Discounted Cashflows and Bond Pricing
# 
#

# fucntion 1
def cashflow_times(n,m):
    """develop the list of the times at which a bond makes coupon payments, with n years and m coupon payments per year
    """
    times = [i for i in range(1, n * m +1)]
    return times


# function 2
def discount_factors(r,n,m):
    """calculate and return a list of discount factors for a given annualized interest rate r, for n years, and m discounting periods per year.
    """
    return [1 /((1 + r / m  ) ** i) for i in cashflow_times(n,m) ]


# function 3
def bond_cashflows(fv,c,n,m):
    """to calculate and return a list of cashflows for a bond specified by the parameters. The parameters are: 
        fv is the future (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year.
    """
    coupon_normal = [fv * c / m for i in cashflow_times(n,m)[:-1]]
    coupon_last = [fv * c / m + fv]
    return coupon_normal + coupon_last


# function 4
def bond_price(fv,c,n,m,r):
    """return the price of a bond. The parameters are: fv is the future (maturity) value of the bond;
       c is the annual coupon rate expressed as percentage per year;
       n is the number of years until maturity;
       m is the number of coupon payments per year;
       and r, the annualized yield to maturity of the bond
    """
    pricelist = [bond_cashflows(fv,c,n,m)[i] * discount_factors(r,n,m)[i] for i in range(0 , n * m )]
    return sum(pricelist)


# funtion 5

def bond_yield_to_maturity(fv, c,n,m,price):
    """to calculate the annualized yield_to_maturity on a bond. The parameters are: fv is the future (maturity) value of the bond;
       c is the annual coupon rate expressed as percentage per year;
       n is the number of years until maturity;
       m is the number of coupon payments per year;
       and price is the current market price of the bond    
    """
    ACCURACY = 0.0001 #iterate until the error is less than $0.0001
 
    upper_bound = 1
    lower_bound = -1
    test_rate = 0
    while abs(price - bond_price(fv,c,n,m,test_rate)) > ACCURACY:
        if price > bond_price(fv,c,n,m,test_rate):
            upper_bound = test_rate
            test_rate = (upper_bound + lower_bound) / 2
           
        elif price < bond_price(fv,c,n,m,test_rate):
            lower_bound = test_rate
            test_rate = (upper_bound + lower_bound) / 2
            
    return test_rate
        
    








if __name__ == '__main__':
    
    print(cashflow_times(5,2))
    print(discount_factors(0.04, 3, 2))
    print(bond_cashflows(100, 0.04, 3, 2))
    print(bond_price(100, 0.04, 3, 2, 0.04))
    print(bond_yield_to_maturity(100,0.04,3,2,101.75))
    
    
    