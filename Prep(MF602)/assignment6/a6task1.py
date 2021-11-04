#
# a6task1.py (Assignment 6, Problem 1)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  Implementing a Matrix as a 2-D List
# 
#

# function 1
def print_matrix(m,label = ''):
    """ takes two parameters, m which is a 2-dimension list (the matrix) and label (a string), and creates a nicely-formatted printout.
    """
    if label != '':
        print(label , '=')
    for i in range(len(m)):
        
        for j in range(len(m[i])):
            if i == 0 and j == 0:
                print('[[',end='')
            if i != 0 and j ==0:
                print(' [',end = '')
            print(f'{m[i][j]:6.2f}',end =',')
            if i != len(m)-1 and j == len(m[0])-1:
                print(']')
            if i ==len(m)-1 and j == len(m[0])-1:
                print(']]')
        print()
        

# # function 2
def zeros(n,m = 0):
    """creates and returns an n * m matrix containing all zeros.
    """
    if m == 0:
        m = n
    s = []
    
    for i in range(n):
        r = []
   
        
        for j in range(m):
            r += [0]
        
        s += [r]
        
    print(print_matrix(s,''))
    
    return s


# function 3
def identity_matrix(n):
    """ creates and returns an n * n identity matrix containing the value of 1 along the diagonal.
    """
    s = zeros(n)
    for i in range(n):
        
        for j in range(n):
            
            if i == j:
                s[i][j] = 1
            
    return s
    


    
# function 4
def transpose(M):
    """creates and returns the transpose of a matrix.
    """
    s = []
    
    for i in range(len(M[0])):
        r = []
        for j in range(len(M)):
            r +=[M[j][i]]
        s += [r]
    return s
    

# function 5
def swap_rows(M, src, dest):
    """perform the elementary row operation that exchanges two rows within the matrix
    """
    if src <= len(M) and dest <= len(M):
    
        memory = M[src][:]
        M[src] = M[dest]
        M[dest] = memory

        return M


# function 6
def mult_row_scalar(M,row,scalar):
    """perform the elementary row operation that multiplies all values in the row row by the numerical value scalar.
    """

        
    a = M[row] 
    r = []
    for i in range(len(M[0])):
        r += [a[i] * scalar]
    M[row]= r
    
    return M
    
    
# function 7
def add_row_into(M, src, dest):
    """performs the elementary-row operation to add the src row into the dest row.
    """
    a = M[src]
    b = M[dest]
    s = []
    for i in range(len(a)):
        s += [a[i] + b[i]]
    M[dest] = s
    
    return M
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    
    # A = [[3,0,2,1],[2,0,-2,3]]
    # print_matrix(A,'A')
    
    # print(zeros(2,3))
    
    # I = identity_matrix(3)
    # print_matrix(I, 'I')
    
    # AT = transpose(A)
    # print_matrix(AT, 'AT')
    
    # B = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    # print_matrix(B)
    # swap_rows(B, 1, 2) # swap rows 1 and 2
    # print_matrix(B)
    
    # C = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    # mult_row_scalar(C, 1, -1) # multiply row 1 by -1
    # print_matrix(C)
    
    A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    add_row_into(A, 2, 1)
    print_matrix(A)
