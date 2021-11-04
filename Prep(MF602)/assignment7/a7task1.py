#
# a7task1.py (Assignment 7, Problem 1)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  In this assignment, you will create a Date class, from which you will be able to create Date objects that represent a day, month, and year. You will add functionality to this class that will enable Date objects to find the day of the week to which they correspond.
# 
#

class Date:
    """You will add functionality to this class that will enable Date objects to find the day of the week to which they correspond.
    """
    
    
#step 1   

    def __init__(self, new_month, new_day, new_year):
        """ It defines the attributes that compose a Date object (month, day, and year) and accepts parameters to set an object’s attributes to some initial values
        """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    
    
    def __repr__(self):
        """This method formats the month, day, and year that represent a Date object into a string of the form 'mm/dd/yyyy' and returns it.
        """
        return f"{self.month:02d}/{self.day:02d}/{self.year}"
    
    def copy(self):
        """returns a newly-constructed object of type Date with the same month, day, and year that the called object has
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    
    
#fucntion 2
    
    def is_leap_year(self):
        """returns True if the called object is in a leap year, and False otherwise
        """

        
        if self.year % 4 != 0 :
            return False
        elif self.year % 100 == 0 and self.year % 400 != 0:
            return False
        
        elif self.year % 100 == 0 and self.year % 400 != 0:
            return True
        
        else:
            return True
        

#function 3

    def is_valid_date(self):
        """returns True if the object is a valid date, and False otherwise
        """
        if self.month > 12 or self.month < 1:
            return False
        
        elif self.month == 4 or self.month==6 or self.month==9 or self.month==11:
            if self.day > 30 or self.day <1:
                 return False
            else:
                return True
     
        
        elif self.month ==1 or self.month == 3 or self.month ==5 or self.month ==7 or self.month ==8 or self.month ==10 or self.month == 12:
            if self.day > 31 or self.day < 1:
                return False
            else:
                return True
        
        elif self.month == 2 and self.is_leap_year() == True:
            if self.day > 29 or self.day <1:
                return False
            else:
                return True
        
        elif self.month == 2 and self.is_leap_year() == False:
            if self.day > 28 or self.day < 1:
                return False
            else:
                return True
        
  

# function 4
    def add_one_day(self):
        """changes the called object so that it represents one calendar day after the date that it originally represented.
        """
        test_day = self
        test_day.day = test_day.day +1
        if test_day.is_valid_date() == True:
            self = test_day
        else:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            
            # elif self.month == 4 or self.month==6 or self.month==9:
            #     self.month += 1
            #     self.day = 1
            else:
                self.day = 1
                self.month += 1
            

# function 5
    def rem_one_day(self):
        """called object so that it represents one calendar day before the date that it originally represented.
        """
        test_day = self
        test_day.day = test_day.day - 1
        
        if test_day.is_valid_date() == True:
            self = test_day
        
        else:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            
            else:
                
                if (self.month -1) == 4 or self.month -1 ==6 or self.month -1 == 9 or self.month -1 == 11:
                    self.day = 30
                elif self.month -1 == 1 or self.month -1 == 3 or self.month -1 == 5 or self.month -1 == 7 or self.month -1 == 8 or self.month -1 == 10 or self.month -1 == 12:
                    self.day = 31
                elif self.month -1 == 2 and self.is_leap_year() == True:
                    self.day = 29
                elif self.month -1 == 2 and self.is_leap_year() == False:
                    self.day = 28
                    
                self.month -= 1
        

# function 6
    def add_n_days(self,n):
        """changes the calling object so that it represents n calendar days after the date it originally represented
        """
        for i in range(n):
            self.add_one_day()

            

        

# function 7
    def rem_n_days(self,n):
        """changes the calling object so that it represents n calendar days before the date it originally represented
        """
        for i in range(n):
            
            self.rem_one_day()

        


# function 8
    def __eq__(self, other):
        """returns True if the called object (self) and the argument (other) represent the same calendar date (i.e., if the have the same values for their day, month, and year attributes). Otherwise, this method should return False.
        """
        if self.month == other.month and self.day == other.day and self.year == other.year:
            return True
        else:
            return False


# function 9
    def is_before(self, other):
        """ returns True if the called object represents a calendar date that occurs before the calendar date that is represented by other.
        """
      
        # if self.year > other.year:
        #     return False
        
        # else:
        #     if self.year == other.year and self.month > other.month:
        #         return False
            
        #     else:
        #         if self.year == other.year and self.month == other.month and self.day >= other.day:
        #             return False
                
        #         else:
        #             return True
        if self.year > other.year:
            return False
        elif self.year < other.year:
            return True
    
        else:
            if self.month > other.month:
                return False
            elif self.month < other.month:
                return True
        
            else:
                if self.day >= other.day:
                    return False
                elif self.day < other.day:
                    return True           

# function 10
    def is_after(self,other):
        """returns True if the calling object represents a calendar date that occurs after the calendar date that is represented by other
        """
    
        # if self.year < other.year:
        #     return False
        
        # else:
        #     if self.year == other.year and self.month < other.month:
        #         return False
            
        #     else:
        #         if self.year == other.year and self.month == other.month and self.day <= other.day:
        #             return False
                
        #         else:
        #             return True
        if self.year < other.year:
            return False
        elif self.year > other.year:
            return True
    
        else:
            if self.month < other.month:
                return False
            elif self.month > other.month:
                return True
        
            else:
                if self.day <= other.day:
                    return False
                elif self.day > other.day:
                    return True          

# function 11
    def diff(self,other):
        """returns an integer that represents the number of days between self and other.
        """
        result = 0
        
        
        copy_other = other.copy()
        copy_self = self.copy()
        while copy_self != copy_other:
            
            if copy_self.is_after(copy_other) == True:

                result += 1
                copy_other.add_one_day()
            
            elif copy_self.is_after(copy_other) == False:
                result = result - 1
                copy_other.rem_one_day()
                
            
        
        return result
                
                
# function 12
    def day_of_week(self):
        """returns a string that indicates the day of the week of the Date object that calls it.
        """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday'] 
        
        origin_date = Date(4,18,2016)
        number = self.diff(origin_date)
        
        if number % 7 == 0:
            return day_of_week_names[0]
        elif number % 7 ==1:
            return day_of_week_names[1]
        elif number % 7 ==2:
            return day_of_week_names[2]
        elif number % 7 ==3:
            return day_of_week_names[3]
        elif number % 7 ==4:
            return day_of_week_names[4]
        elif number % 7 ==5:
            return day_of_week_names[5]
        elif number % 7 ==6:
            return day_of_week_names[6]
            
        
            












if __name__ == '__main__':
    
    # d1 = Date(1, 1, 2020)
    # d2 = Date(1, 1, 2021)
    # d1 = Date(8,25,2021)
    # d3 = Date(2,30,2020)
    # d4 = Date(2,29,2020)
    # d6 = Date(-4,-4, -5)
    # d7 = Date(2,29,2100)
    # d1 = Date(12, 31, 2020)
    # d2 = Date(2, 28, 2020)
    
    # ny = Date(1, 1, 2022)
    # d = Date(8, 25, 2021)
    # d3 = Date(12,31,2021)
    # d4 = Date(12,31,2022)
   
    # d1 = Date(8, 25, 2021)
    # d2 = Date(9, 1, 2021)
    # d3 = Date(8, 25, 2021)
    # d4 = Date(4, 18, 2022)
    
    d = Date(4, 18, 2022)
