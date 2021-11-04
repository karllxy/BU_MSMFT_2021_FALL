#loop

for i in [3,4,5]:
    print('warning')
    print(i)
     # in the loop


for val in [2,4,6,8,10]:
    print(val * 10)
 # not in the loop


def print_square(numbers):
    for num in numbers:
        print (num**2)



#range
def sum(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
        
    return result


def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
        

# combination
def find_min(numbers):
    minv = numbers[0]
    if len(numbers) == 1:
        return minv
    else:
        for i in numbers:
            if i <= minv:
                minv = i
        return minv


# Accumulating a list
def fib(n):
    fib_numbers = [0,1]
    for i in range(2,n):
        next_fib = fib_numbers[i-1] + fib_numbers[i-2]
            
        fib_numbers += [next_fib]
    return fib_numbers[:n]



# Processing a CSV file





if __name__ == '__main__':
    
    
    print(i)
    print(val)
    print_square([7,8,9]) #this would not print none.
   # print(print_square([7,8,9])) this woul contain None.
    print(list(range(2,12)))
    print(list(range(0,50,7)))
    print(list(range(50,0,-7)))
    print(sum([10,20,30,40,50]))
    print(fact(5))
    print(find_min([5,6,7,3,2]))
    print(fib(2))
    