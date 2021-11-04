# 
# a4task2.py - Assignment 4, Task 2
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Simulating a Bond Auction
# 
#

# function 1
def collect_bids(filename):
    """process the data file containing the bids
    """
    
    f = open(filename, 'r')
    empty_list = []
    for line in f.readlines()[1:]:
        line = line[:-1]
        fields = line.split(',')
        linelist = [int(fields[0]),int(fields[1]),float(fields[2])]
        empty_list += [linelist]
        
    f.close()
    return empty_list




# function 2
def print_bids(bids):
    """rocess the a of bids, and produce a beautifully-formatted table of the bids. In your function, you will process a list containing bids one line at a time.
    """
    print('Bid ID          Bid Amount          Price  ')
    for i in range(0, len(bids)):
        a = bids[i]
        print(f"{a[0]:6.0f} {'       $'}{a[1]:9.0f}{'        $'} {a[2]:8.3f}\n")
        

# function 3
from a4task1 import *

def find_winning_bids(bids,total_offering_fv,c,n,m):
    """processes a list of bids and determine which are successful in the auction. The parameters are:
bids, where each bid is a sublist in the form of [bid_id, bid_amount, bid_price],
total_offering_fv is the total amount of bonds being sold,
c is the annualized coupon rate,
n is the number of years to maturity for the bonds, and
m is the number of coupon payments per year.
    """
    empty = []
    for i in range(len(bids)):
    
        a = bids[i]
        empty += [[a[2],a[0],a[1]]]
    
    empty.sort()
    empty.reverse()  
    
    amount_reverse =[]
    bids_reverse = []
    for i in range(len(empty)):
    
        b = empty[i]
        bids_reverse += [[b[1],b[2],b[0]]] 
        amount_reverse += [b[2]]
    print('Here are all of the bids, sorted by price descending: ')
    
    print_bids(bids_reverse)
    
    print('The auction is for $ '+ format(total_offering_fv,'.2f') + ' of bonds.')
    
    amount_winning = []
    number = 0
    for i in range(len(amount_reverse)):
        if total_offering_fv > amount_reverse[i]:
            number += 1
            amount_winning += [amount_reverse[i]]
            total_offering_fv = total_offering_fv - amount_reverse[i]
        elif total_offering_fv < amount_reverse[i] and total_offering_fv > 0:
            number += 1
            amount_winning += [total_offering_fv]
            total_offering_fv = total_offering_fv - amount_reverse[i]
        elif total_offering_fv < amount_reverse[i] and total_offering_fv <= 0:
            amount_winning += [0]
    
    
    clearing_price = bids_reverse[number-1][2]
    
    YTM = bond_yield_to_maturity(100, c,n,m,clearing_price)

    print(str(number) + ' bids were successful in the auction.')
    print('The auction clearing price was $'+ str(clearing_price)+',i.e. YTM is ' + format(YTM,'.6f')+' per year.')
    print('Here are the results for all bids:')
    
    bids_end = []
    
    for i in range(len(bids_reverse)):
        c = bids_reverse[i]
        bids_end += [[c[0],amount_winning[i],c[2]]]

    print_bids(bids_end)
    return bids_end
        
    

  
            







    
    
    
    
    
    

if __name__ == '__main__':
    bids = collect_bids('./bond_bids.csv')
    print("Here are all the bids: ")
    print(bids)
    print_bids(bids)
    print()
    processed_bids = find_winning_bids(bids, 1400000, 0.0325, 5, 2)
    print(processed_bids)
    