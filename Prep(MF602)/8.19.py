#list comprehesion

def perfect_squares(values):
    answer = [x for x in values if x ** 0.5 == int(x **0.5) ]
    return answer


def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
        

def generate_primes(n):
    return [x for x in range(n) if is_prime(x) == True]


# the shortest way for numvowels
def num_vowels(s):
    lc = [1 for c in s if c in 'aeiou']
    return sum(lc)
    
    



# the indefinite loop (While loop)
def guessing_game():
    import random
    secret = random.randint(1,10)
    guess = int(input('Guess a number between 1 and 10:'))
    while guess != secret:
        print('Wrong')
        if guess > secret:
            print('too high')
        elif guess < secret:
            print('too low')
        guess = int(input('Guess a number between 1 and 10:'))
    print('you are correct.')









    
if __name__ == '__main__':
    
    #print(generate_primes(100))
    guessing_game()
    