#
# a7task2.py (Assignment 7, Problem 2)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Some Date clients
# 
#
from a7task1 import Date

# function 1
def options_expiration_days(year):
    """returns a list of all of the Dates on which options expire during a calendar year
    """
    number = 0
    result = []
    for i in range(1,13):
        begin_date = Date(i,1,year)
        
        begin_date_week = begin_date.day_of_week()
        if begin_date_week == 'Saturday':
            number = 6
        elif begin_date_week == 'Sunday':
            number = 5
        elif begin_date_week == 'Monday':
            number = 4
        elif begin_date_week == 'Tuesday':
            number = 3
        elif begin_date_week == 'Wednesday':
            number = 2
        elif begin_date_week == 'Thursday':
            number = 1
        elif begin_date_week == 'Friday':
            number = 0
        
        number += 14
        
        test_date = begin_date.copy()
        test_date.add_n_days(number)

        result += [test_date]
    


        
    
    return result
        

# function 2
def find_NYD(year):
    result = []
    begin_date = Date(1,1,year)
    
    if begin_date.day_of_week() == 'Sunday':
        begin_date.add_one_day()
        result += [begin_date]
    
    else:
        result += [begin_date]
       
    print('New Year"s Day is observed on ' +begin_date.day_of_week()+' '+str(result[0]))
    return result




def find_mlkd(year):
    """Find the Martin Luther King Day of certain year
    """
    result = []
    number = 0
    begin_date = Date(1,1,year)
    begin_date_week = begin_date.day_of_week()
    if begin_date_week == 'Saturday':
        number = 2
    elif begin_date_week == 'Sunday':
        number = 1
    elif begin_date_week == 'Monday':
        number = 0
    elif begin_date_week == 'Tuesday':
        number = 6
    elif begin_date_week == 'Wednesday':
        number = 5
    elif begin_date_week == 'Thursday':
        number = 4
    elif begin_date_week == 'Friday':
        number = 3   
    number += 14
    

        
    test_date = begin_date.copy()
    test_date.add_n_days(number)

    result += [test_date]
    print('Martin Luther King Day is observed on ' +test_date.day_of_week()+' '+str(result[0]))
    return result


def find_PD(year):
    result = []
    number = 0
    begin_date = Date(2,1,year)
    begin_date_week = begin_date.day_of_week()
    if begin_date_week == 'Saturday':
        number = 2
    elif begin_date_week == 'Sunday':
        number = 1
    elif begin_date_week == 'Monday':
        number = 0
    elif begin_date_week == 'Tuesday':
        number = 6
    elif begin_date_week == 'Wednesday':
        number = 5
    elif begin_date_week == 'Thursday':
        number = 4
    elif begin_date_week == 'Friday':
        number = 3   
    number += 14
    

        
    test_date = begin_date.copy()
    test_date.add_n_days(number)

    result += [test_date]
    
    print('President"s Day is observed on ' +test_date.day_of_week()+' '+str(result[0]))
    return result
    

def find_ID(year):
    result = []
    begin_date = Date(7,4,year)
    
    if begin_date.day_of_week() == 'Sunday':
        begin_date.add_one_day()
        result += [begin_date]
    
    else:
        result += [begin_date]    
    print('Independence Day is observed on ' +begin_date.day_of_week()+' '+str(result[0]))
    return result



def find_LD(year):
    result = []
    number = 0
    begin_date = Date(9,1,year)
    begin_date_week = begin_date.day_of_week()
    if begin_date_week == 'Saturday':
        number = 2
    elif begin_date_week == 'Sunday':
        number = 1
    elif begin_date_week == 'Monday':
        number = 0
    elif begin_date_week == 'Tuesday':
        number = 6
    elif begin_date_week == 'Wednesday':
        number = 5
    elif begin_date_week == 'Thursday':
        number = 4
    elif begin_date_week == 'Friday':
        number = 3   
    

        
    test_date = begin_date.copy()
    test_date.add_n_days(number)

    result += [test_date]
    print('Labor Day is observed on ' +test_date.day_of_week()+' '+str(result[0]))
    return result    




def find_TGD(year):
    result = []
    number = 0
    begin_date = Date(11,1,year)
    begin_date_week = begin_date.day_of_week()
    if begin_date_week == 'Saturday':
        number = 5
    elif begin_date_week == 'Sunday':
        number = 4
    elif begin_date_week == 'Monday':
        number = 3
    elif begin_date_week == 'Tuesday':
        number = 2
    elif begin_date_week == 'Wednesday':
        number = 1
    elif begin_date_week == 'Thursday':
        number = 0
    elif begin_date_week == 'Friday':
        number = 6  
    number += 21
    

        
    test_date = begin_date.copy()
    test_date.add_n_days(number)

    result += [test_date]
    print('Thanksgiving Day is observed on ' +test_date.day_of_week()+' '+str(result[0]))
    return result        


def find_CD(year):
    result = []
    begin_date = Date(12,25,year)
    
    if begin_date.day_of_week() == 'Sunday':
        begin_date.add_one_day()
        result += [begin_date]
    
    else:
        result += [begin_date]    
    print('Christmas Day is observed on ' +begin_date.day_of_week()+' '+str(result[0]))
    return result


def find_MD(year):
    result = []
    begin_date = Date(6,1,year)
    number = 0
    begin_date_week = begin_date.day_of_week()
    if begin_date_week == 'Saturday':
        number = 5
    elif begin_date_week == 'Sunday':
        number = 6
    elif begin_date_week == 'Monday':
        number = 7
    elif begin_date_week == 'Tuesday':
        number = 1
    elif begin_date_week == 'Wednesday':
        number = 2
    elif begin_date_week == 'Thursday':
        number = 3
    elif begin_date_week == 'Friday':
        number = 4  
    
    test_date = begin_date.copy()
    test_date.rem_n_days(number)

    result += [test_date]
    print('Memorial Day is observed on ' +test_date.day_of_week()+' '+str(result[0]))
    return result      






def market_holidays(year):
    """ returns a list of the Dates of all market holidays for a given year
    """
    NYD = find_NYD(year)
    MLKD = find_mlkd(year)
    PD = find_PD(year)
    MD = find_MD(year)
    ID = find_ID(year)
    LD = find_LD(year)
    TGD = find_TGD(year)
    CD = find_CD(year)
    print()
    
    
    holidays = []
    holidays = NYD + MLKD + PD + MD + ID + LD + TGD + CD
    return holidays


















if __name__ == '__main__':
    
    options_expiration_days(2021)
    holidays = market_holidays(2021)
    
                
        
        