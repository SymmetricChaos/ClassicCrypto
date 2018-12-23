import string
from MathFunctions import primes

# Godel's encoding is not technically a cipher, it is a code, but it is 
# included here simply because it is an interesting method of encoding text
# as numbers.

# It works like this. Each letter is assigned a number. Then the first letter
# of the word is 2 to the power of that number. The second letter is equal to
# 3 to the power of that number. And so on for the prime numbers. Then all 
# those numbers are multiplied together. The process starts again for the next
# word in the text.

# Godel encoding is extremely inefficient in terms of storage space. The 
# resulting numbers are often extremely large.

def godelencoding(S,decode=False):
    
    if decode == False:
        alpha = string.ascii_uppercase
        D = {x:ord(x)-64 for x in alpha}
        
        out = 1
            
        for let,pr in zip(S,primes()):
            out *= pr**D[let]
                
        return out

def godelcode(S,decode=False):
    if decode == False:
        T = S.split(" ")
        L = []
        for i in T:
            L.append(str(godelencoding(i)))
        return " ".join(L)

    if decode == True:
        out = []
        N = S.split(" ")
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
