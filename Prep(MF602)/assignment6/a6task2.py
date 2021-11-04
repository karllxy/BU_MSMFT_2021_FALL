#
# a6task2.py (Assignment 6, Problem 2)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description:  Matrix Operations
# 
#
from a6task1 import *

# function 1
def add_matrices(A,B):
    """takes as parameters 2 matrices (2d lists) and returns a new matrix which is the element-wise sum of the matrices A and B
    """
    assert len(A) == len(B) and len(A[0]) == len(B[0]),'Assertion Error : incompatible dimensions : cannot add ('+str(len(A))+','+str(len(A[0]))+') with ('+str(len(B))+','+str(len(B[0]))+') !'
 
    

    s = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[i])):
            r += [A[i][j]+B[i][j]]
            
        s += [r]
        
    return s

# function 2
def sub_matrices(A,B):
    """takes as parameters 2 matrices (2d lists) and returns a new matrix which is the element-wise difference of the matrices A and B
    """
    assert len(A) == len(B) and len(A[0]) == len(B[0]),'Assertion Error : incompatible dimensions : cannot sub ('+str(len(A))+','+str(len(A[0]))+' ) with ('+str(len(B))+','+str(len(B[0]))+') !'
        
    

        
    s = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[i])):
            r += [A[i][j]-B[i][j]]
            
        s += [r]
        
    return s


# function 3
def mult_scalar(M,s):
    """returns a new matrix containing the values of the original matrix multiplied by the scalar value
    """
    L = []
    
    for i in range(len(M)):
        r = []
        
        for j in range(len(M[i])):
            r += [ M[i][j] * s ]
            
        L += [r]
        
    return L


# function 4
def helpro(A,B):
    s = 0
    for i in range(len(A)):
        s += A[i] * B[i]
        
    return s
        
    

def dot_product(M , N):
    """ takes as parameters two matrices M and N, and returns a new matrix containing dot product of these matrices
    """
    s = []

    if len(M[0]) != len(N):
        print('Assertion Error : incompatible dimensions : cannot dot-product ('+str(len(M))+','+str(len(M[0]))+' ) with ('+str(len(N))+','+str(len(N[0]))+') !')
    
    else:
        s = []
        
        V = transpose(N)
        for i in range(len(M)):
            r = []
            
            for j in range(len(V)):
                
                r += [helpro(M[i],V[j])]
            
            s += [r]
            
        return s


# function 5
def create_sub_matrix(M, exclude_row, exclude_col):
    """returns a sub-matrix of M, with all values that are not in row exclude_row or column exclude_col.
    """

    s = []
    for i in range(len(M)):
        if i != exclude_row:
            
            s += [M[i]]
        else:
            s += []
           
    s = transpose(s)

    r = []

    for j in range(len(s)):
        if j != exclude_col:
          
            r += [s[j]]

        else:
            r += []
        
    r = transpose(r)
    
    return r

# function 6
def determinant(M):
    """takes a parameter M that is a (non-singular) matrix, and returns its determinant
    """
    assert len(M) == len(M[0]), 'Assertion Error : incompatible dimensions :  ('+str(len(M))+','+str(len(M[0]))+') !'
    result = 0
    if len(M) == 1:
        result = int(M[0][0])

    elif len(M) == 2:
        result = int(M[0][0]) * (M[1][1]) - int(M[0][1]) * int(M[1][0])
    else:
        for i in range(len(M)):
            result += int(M[0][i]) * ((-1)**i) * int(determinant(create_sub_matrix(M, 0, i)))
    
    return result
    

# function 7
def matrix_of_minors(M):
    """takes a matrix and returns the corresponding matrix of minors
    """
    s = []
    for i in range(len(M)):
        r = []
        
        for j in range(len(M[i])):
            r += [determinant(create_sub_matrix(M, i, j))]
        
        s += [r]
    return s


# function 8
def inverse_matrix(M):
    """takes a parameter that is a (non-singular) matrix, and returns its inverse
    """
    N = matrix_of_minors(M)
    s = []
    for i in range(len(N)):
        r =[]
        for j in range(len(N[i])):
            
            r += [N[i][j]*(-1) ** (i+j)]
            
        
        s += [r]
        
    num = 1 / determinant(M)
    t = transpose(s)
    inverse = mult_scalar(t,num)
    return inverse
       
 
                    
            
                













if __name__ == '__main__':
    
    # A = [[1,2,3],[4,5,6]]
    # B = [[4,5,6],[1,2,3]]
    # # S = sub_matrices(A, B)
    # # print_matrix(S, 'S')
    # A = [[3,0,2,1],[2,0,-2,3]]
    # print_matrix(A)

    # B = mult_scalar(A, 3)
    # print_matrix(B)
    
    # A = [[1,2,3],[4,5,6]]   
    # B = [[3,2],[4,1],[5,0]]
    # P = dot_product(A,B)
    # print_matrix(P, 'P')

    # A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # print_matrix(create_sub_matrix(A, 0, 0))
    
    # A = [[3,4],[8,6], [10,7]]
    # d = determinant(A)
    # print(d)
    
    A = [[3,0,2],[2,0,-2],[0,1,1]]
    print_matrix(A, 'A')
    M = matrix_of_minors(A)
    print_matrix(M,'m')
    AI = inverse_matrix(A)
    print_matrix(AI,'AI')
    
    # A = [[3,0,2,1],[2,0,-2,3]]
    # print_matrix(A)
    # B = mult_scalar(A, 3)
    # print_matrix(B)
