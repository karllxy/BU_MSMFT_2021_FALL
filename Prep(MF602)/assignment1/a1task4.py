# 
# a1task4.py - Assignment 1, Task 4
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: The Life-Cycle Model of Saving and Consumption
# 
#
from a1task3 import *

def life_cycle_model():
    """
    This function stimulates the life-cycle model of savinf and consumption.
    """

    r = float(input('Enter the current inflation-indexed risk-free rate of return:'))
    age_now = int(input('Enter your age now:'))
    age_retire = int(input('Enter your expected retirement age:'))
    pv_income = int(input('Enter your current annual income:'))
    consumption = 100 - age_now
    n1 = age_retire - age_now
    human_capital = int(pv_annuity(r, n1, pv_income))
    print('You have ' + str(n1) + ' remainning working years with an income of $' + str(pv_income) + ' per year. The present value of your human capital is about $' + str(human_capital) )

    assets = int(input('Enter the value of your financial assets: '))

    net_worth = human_capital + assets
    sustainable = int(annuity_payment(r,consumption, net_worth))
    save = int(pv_income - sustainable)



    
    print('Your economic net worth is: $' + str(net_worth) + ' per year.')
    print('Your sustainable standard of living is about $' + str(sustainable)+ ' per year.')
    print('To achieve this standard of living to age 100, you must save $' + str(save) + ' per year.')

if __name__ == '__main__':

        life_cycle_model()