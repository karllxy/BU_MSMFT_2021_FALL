def is_before(self, other):
    
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