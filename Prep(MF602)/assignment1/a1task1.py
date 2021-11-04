# 
# a1pr1.py - Assignment 1, task 1
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Indexing and slicing puzzles
#
# This is an individual-only problem that you must complete on your own.
# 

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:] 
print(answer0)

# Solve puzzles 1-4 here:

# Puzzle 1
# Creating the list [2,7] from pi and e
answer1 = e[0:2]
print(answer1)

#Puzzle 2
#Creating the list [5,4,3] from pi and e
answer2 = pi[4:1:-2] + [pi[0]]
print(answer2)

#Puzzle 3
#Creating the list [3,5,7] from pi and e
answer3 = pi[0:5:4] + [e[1]]
print(answer3)

#Puzle 4
# Creating the list [1,2,3,4,5] from and e
answer4 = [e[2]] + [e[0]] + pi[0:6:2]
print(answer4)






#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]

# Solve puzzles 5-10 here:
    
# Puzzle 6
# Creating the string 'universe'
answer6 = u[0:7] + t[1]

# Puzzle 7
# Creating the string 'roster'
answer7 = u[5] + b[1:4] + t[1:3]

# Puzzle 8
# Creating the string 'boisterous'
answer8 = b[0:2] + u[7:5:-1] + t[0:3] + b[1] + u[0:7:6]

# Puzzle 9
# Creating the string 'yesyesyes'
answer9 = 3*(u[9:3:-5] + b[2])

# Puzzle10
# Creating the string 'trist'
answer10 = t[0:5:2] + u[6:9:2]
