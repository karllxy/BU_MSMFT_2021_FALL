# 
# a1task3.py - Assignment 1, Task 3
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Functions for time value of money calculations
# 
#
def fv_lump_sum(r,n,pv):
    """returns the future value of a lump sump pv invested 
    at the periodic rate r for n periods
    """
    return pv * (1 + r ) ** n

def pv_lump_sum(r,n,fv):
    """return the present value of a lump sum fv to be received in the future, 
    discounted at the periodic rate r for n periods
    """
    return fv/((1+r)**n)

def fv_annuity(r,n,pmt):
    """return the future value of an annuity of pmt to be received each period 
    for n periods, invested at the periodic rate r.
    """
    return (pmt*((1+r)**n - 1) / r)
    
def pv_annuity(r,n,pmt):
    """eturn the present value of an annuity of pmt to be received each period for n periods, 
    discounted at the rate r.
    """
    return pmt*(1-(1+r)**(-n) ) / r

def annuity_payment(r,n,pv):
    """alculates the annuity payment for a present value of pv 
    to be repaid at a periodic interest rate of r for n periods
    """
    return r*pv / (1-(1+r)**(-n))
    
    
    # Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':
    
    # $100 at 5% rate for 2 years
    print('fv_lump_sum(0.05, 2, 100)',fv_lump_sum(0.05, 2, 100))
    
    # $500 received in 5 years, 6% APR, semi-ann. compounding
    print('pv_lump_sum(0.06/2, 5*2, 500)',pv_lump_sum(0.06/2, 5*2, 500))
    
    # invest $100 per year for 5 years at 4% interest
    print('fv_annuity(0.04, 5, 100)',fv_annuity(0.04, 5, 100))
    # invest $100 per month for 10 years at 9% APR
    print('fv_annuity(0.09/12, 10*12, 100)',fv_annuity(0.09/12, 10*12, 100))
    
    # pv of 30 payments of $250 per year, 5% interest
    print('pv_annuity(0.05, 30, 250)',pv_annuity(0.05, 30, 250))
    # pv of 60 payments of $471.75 per month, 0.9% APR
    print('pv_annuity(0.009/12,60, 471.75)',pv_annuity(0.009/12,60, 471.75))  
    
    # annuity payment for pv of $1,000 for 10 year at 5%
    print('annuity_payment(0.05, 10, 1000)',annuity_payment(0.05, 10, 1000))
    # annuity payment for pv of $27,667 for 60 months at 0.9% APR
    print('annuity_payment(0.009/12, 60, 27667.44)',annuity_payment(0.009/12, 60, 27667.44))