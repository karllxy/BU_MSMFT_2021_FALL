# nested loop

def print_products(m,n):
    """formatted table of the products of 1...m times 1...n
    """
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(f"{i * j:8d}" ,end='') # print all columns in  for one row
        print() #line break





def print_grint(values):
    for i in range(len(values)):
        
        for j in range(len(values[i])):
            
            print(f"{values[i][j]:8d}" , end='')
        print()


def sum_2d(values):
    s = 0
    for i in range(len(values)):
        
        for j in range(len(values[i])):
            s += values[i][j]
    
    return s























if __name__ == '__main__':
    
    print_products(8,4)
    
    print()
    
    mylist = [[17,2], [2,5], [1,3,7]]
    print_grint(mylist)
    
    print(sum_2d(mylist))
    
    