import string
from UtilityFunctions import primes

# The notion of a Godel number is an unusual method of encoding information
# devised by Kurt Godel as a step in hproving his two famous incompleteness 
# theorems. For him it was a method for representing mathematical forumlas but
# it can be easily adapted to encoding words instread.

# It works like this. Each letter is assigned a number. Then the first letter
# of the word is 2 to the power of that number. The second letter is equal to
# 3 to the power of that number. And so on for the prime numbers. Then all 
# those numbers are multiplied together. The process starts again for the next
# word in the text.

# Using Godel numbers is, as a rule, tremendously inefficient as the numbers
# that result are quite large.

# For compatibility with other functions in the project the encoding is 
# returned as a string not as a list of numbers. The "sep" keyword allows the 
# user to specify what it used to separate the numbers of the godel encoding. 

def godelNumber(S,decode=False):
    
    if decode == False:
        alpha = string.ascii_uppercase
        D = {x:ord(x)-64 for x in alpha}
        
        out = 1
            
        for let,pr in zip(S,primes()):
            out *= pr**D[let]
                
        return out

def godelCode(S,decode=False,sep=" "):
    if decode == False:
        T = S.split(" ")
        L = []
        for i in T:
            L.append(str(godelNumber(i)))
        return sep.join(L)

    if decode == True:
        out = []
        N = S.split(sep)
        for n in N:
            t = int(n)
            for p in primes():
                ctr = 0
                while t % p == 0:
                   ctr += 1
                   t = t // p
                out.append(chr(ctr+64))
                if t == 1:
                    break
            out.append(" ")
        return "".join(out)
