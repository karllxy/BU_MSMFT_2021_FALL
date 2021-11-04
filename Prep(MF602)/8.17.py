def smaller(x,y,z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z






def hasvowel(s):
    if 'a' in s:
        return True
    if 'e' in s:
        return True
    if 'i' in s:
        return True
    if 'o' in s:
        return True
    if 'u' in s:
        return True
    # if 'a' or 'e' or 'i' or 'o' or 'u' in s:
    else:
        return False
    
    
    # Note: Functions calling other functions!

# Functions calling themselves: recursion.

# Use rest to hold the results.
 
def power(b,p):
    print('power(',b,',',p,')')
    if p == 0:
        print('power(',b,',',p,')','base case, returning 1')
        return 1
    if p > 0:
        rest = power(b,p-1)
        print('power(',b,',',p,')','recursive case, returning', b*rest)
        return b*rest












def num_vowels(s):
     print('num_vowels(',s,')')
     if s == '':
         return 0
     
     num_rest = num_vowels(s[1:])
     if s[0] in 'aeiou':
         print('num_vowels(',s,'),returning', 1 + num_rest)
         return 1 + num_rest
     else:
         print('num_vowels(',s,'),returning',num_rest)
         return num_rest
 








if __name__ == '__main__':
    
    print('smaller(20,4,17)',smaller(20,4,17))
    print('smaller(18,8,4)',smaller(18,8,4))
    print('hasvowel(''finance'')',hasvowel('finance'))
    print('power(2,3)',power(2,3))
    print('num_vowels(''finance'')',num_vowels('finance'))


